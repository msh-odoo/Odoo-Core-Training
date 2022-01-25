from odoo import _, api, fields, models


class SessionWizard(models.TransientModel):
    _name = 'session.assign.instructor'

    instructor_id = fields.Many2one("res.partner", "Instructor", required=True)

    def action_assign_session(self):
        self.ensure_one()
        activeIds = self.env.context.get('active_ids')
        self.env['course.session'].browse(activeIds).write({'instructor_id': self.instructor_id.id})
        return True

    # TODO: Add many2many relation with attendees and add attendees from Wizard
