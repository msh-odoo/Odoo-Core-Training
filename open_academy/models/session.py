from odoo import _, api, fields, models

class Session(models.Model):
    _name = "course.session"

    name = fields.Char()
    course_id = fields.Many2one('course.course', string="Course")
    attendee_ids = fields.Many2many('res.partner')
    start_datetime = fields.Datetime()
    end_datetime = fields.Datetime()

    def action_confirm(self):
        for session in self:
            for attendee in session.attendee_ids:
                print ("Attendee ::: ", attendee.name)
