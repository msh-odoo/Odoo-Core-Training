from odoo import api, models, fields

class Course(models.Model):
    _name = "course.course"

    name = fields.Char(string="Name of the Course", help="This contains course name", copy=False, required=True, translate=True)
    description = fields.Html(readonly=True, states={'new': [('readonly', False)]})
    state = fields.Selection([('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default="new")
    active = fields.Boolean(default=True)

    session_ids = fields.One2many('course.session', 'course_id', string="Sessions")

    def action_confirm(self):
        self.state
        return True

    def write(self, vals):
        for record in self:
            print ("\n\nrecord name is ::: ", record.name)
        return super().write(vals)
