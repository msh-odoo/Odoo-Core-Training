from odoo import _, api, fields, models
from odoo.exceptions import UserError

from dateutil.relativedelta import relativedelta

class Session(models.Model):
    _name = "course.session"

    @api.depends('start_datetime', 'end_datetime')
    def _get_duration(self):
        for record in self:
            if record.end_datetime and record.start_datetime:
                diff = record.end_datetime - record.start_datetime
                record.duration = diff.days
            else:
                record.duration = 1

    def _set_duration(self):
        for record in self:
            record.end_datetime = record.start_datetime + relativedelta(days=record.duration)

    def _search_duration(self, operator, value):
        self.env.cr.execute("SELECT id from course_session where end_datetime::DATE - start_datetime::DATE %s %s" %(operator, value))
        ids = self.env.cr.fetchall()
        return [('id', 'in', [id[0] for id in ids])]

    name = fields.Char()
    course_id = fields.Many2one('course.course', required=True, string="Course")
    attendee_ids = fields.Many2many('res.partner')
    instructor_id = fields.Many2one('res.partner')
    start_datetime = fields.Datetime()
    end_datetime = fields.Datetime()
    duration = fields.Float(compute=_get_duration, inverse=_set_duration, search=_search_duration)
    course_name = fields.Char(related="course_id.name", string="Course Name")

    @api.onchange('course_id')
    def _onchange_course_id(self):
        self.name = self.course_id.name

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor(self):
        if self.instructor_id in self.attendee_ids:
            raise UserError(_("Instructor should not be Attendee of the session."))

    def action_confirm(self):
        for session in self:
            for attendee in session.attendee_ids:
                print ("Attendee ::: ", attendee.name)

    def create(self, vals_list):
        res = super(Session, self).create(vals_list)
        # my logic here
        return res