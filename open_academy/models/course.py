from odoo import api, fields, models

class Course(models.Model):
    _name = "course.course"

    name = fields.Char(help="Course Name")
    description = fields.Html(string="Course Details", copy=False, states={'new': [('readonly', False)]}, readonly=True)
    state = fields.Selection([('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default="new")
    active = fields.Boolean(default=True)
