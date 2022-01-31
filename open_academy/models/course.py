from odoo import _, api, fields, models
from odoo.exceptions import UserError

class Course(models.Model):
    _name = "course.course"
    _description = "Course"

    name = fields.Char(help="Course Name", required=True)
    description = fields.Html(string="Course Details", copy=False, states={'new': [('readonly', False)]}, readonly=True)
    state = fields.Selection([('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default="new")
    active = fields.Boolean(default=True)
    session_ids = fields.One2many('course.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('course_value_unique', 'unique(name)', "Couse name should be unique.")
    ]

    def name_get(self):
        final_result = []
        result = super().name_get()
        if not self.env.context.get('show_state'):
            return result
        for item in result:
            final_result.append((item[0], item[1] + " (" + self.browse(item[0]).state + ")"))
        return final_result

    @api.constrains('state', 'session_ids')
    def _check_sessions(self):
        for record in self:
            if record.state == 'confirm' and not len(record.session_ids):
                raise UserError(_("You can not confirm Course if there are no sessions."))

    def action_confirm(self):
        return self.write({'state': 'confirm'})

    def action_cancel(self):
        return self.write({'state': 'cancel'})