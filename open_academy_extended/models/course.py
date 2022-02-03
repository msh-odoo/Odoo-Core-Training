from odoo import _, api, fields, models

class Course(models.Model):
    _inherit = "course.course"

    course_price = fields.Float()


class CrashCourse(models.Model):
    _name = "crash.course"
    _inherit = "course.course"

    course_start_date = fields.Date("Start Date")
    course_end_date = fields.Date("End Date")


class SpecialCourse(models.Model):
    _name = "special.course"
    _inherits = {'course.course': 'course_id'}

    course_id = fields.Many2one('course.course', string="Course")
    special_price = fields.Float()
