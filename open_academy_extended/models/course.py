from odoo import _, api, fields, models

class Course(models.Model):
    _inherit = "course.course"

    internal_details = fields.Text()


class CrashCourse(models.Model):
    _name = "crash.course"
    _inherits = {'course.course': 'course_id'}

    course_id = fields.Many2one('course.course')
    additional_details = fields.Text()
