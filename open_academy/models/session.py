from dateutil.relativedelta import relativedelta
from odoo import _, api, fields, models

class Session(models.Model):
    _name = "course.session"

    @api.depends('start_datetime', 'end_datetime')
    def _get_duration(self):
        for record in self:
            if record.start_datetime and record.end_datetime:
                diff = record.end_datetime - record.start_datetime
                record.duration = diff.days

    def _inverse_duration(self):
        for record in self:
            record.end_datetime = record.start_datetime + relativedelta(days=record.duration)

    def _search_duration(self, operator, value):
        self.env.cr.execute("SELECT id from course_session where end_datetime::DATE - start_datetime::DATE %s %s" %(operator, value))
        datas = self.env.cr.fetchall()
        return [('id', 'in', [data[0] for data  in datas])]

    name = fields.Char(string="Name", required=True)
    description = fields.Html()
    start_datetime = fields.Datetime()
    end_datetime = fields.Datetime()
    course_id = fields.Many2one('course.course', string="Course")
    instructor_id = fields.Many2one('res.partner')
    attendee_ids = fields.Many2many('res.partner', striing="Attendees", copy=False)
    duration = fields.Float(compute="_get_duration", inverse="_inverse_duration", search="_search_duration")
    course_name = fields.Char(related="course_id.name")

    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id:
            self.description = self.course_id.description
            self.instructor_id = self.env['res.partner'].search([], limit=1)

    @api.onchange('instructor_id')
    def _onchange_instructor_id(self):
        if self.instructor_id:
            self.name = self.instructor_id.name + '\'s Session'
