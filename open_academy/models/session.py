from odoo import _, api, fields, models

class Session(models.Model):
    _name = "course.session"

    name = fields.Char()
    start_datetime = fields.Datetime()
    end_datetime = fields.Datetime()
    course_id = fields.Many2one('course.course', string="Course")
    attendee_ids = fields.Many2many('res.partner', striing="Attendees")