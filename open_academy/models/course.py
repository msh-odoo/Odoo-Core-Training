from odoo import _, api, models, fields
from odoo.exceptions import UserError

class Course(models.Model):
    _name = "course.course"

    name = fields.Char(string="Name of the Course", help="This contains course name", copy=False, required=True, translate=True)
    description = fields.Html(readonly=True, states={'new': [('readonly', False)]})
    state = fields.Selection([('new', 'New'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default="new")
    active = fields.Boolean(default=True)

    session_ids = fields.One2many('course.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('course_value_unique', 'unique(name)', "Couse name should be unique.")
    ]

    @api.constrains('session_ids', 'state')
    def _check_sessions(self):
        print ("\n\nInside _check_sessions ::: ", self)
        for record in self:
            if record.state and record.state == 'confirm' and not len(record.session_ids):
                raise UserError(_("You can not confirm Course if there are no Sessions."))

    def action_confirm(self):
        return self.with_context({'test': True}).write({'state': 'confirm'})

    def write(self, vals):
        for record in self:
            print ("\n\nrecord name is ::: ", record.name)
        if self.env.context.get('test'):
            pass
            # Your logic to perform something
        return super().write(vals)
    