from odoo import _, api, fields, models

class AssignInstructor(models.TransientModel):
    _name = "assign.instructor"

    instructor_id = fields.Many2one("res.partner", string="Instructor")

    def action_assign_instructor(self):
        self.ensure_one()
        Session = self.env['course.session']
        ids = self.env.context.get('active_ids')
        sessions = Session.browse(ids)
        sessions.write({'instructor_id': self.instructor_id})
        return True