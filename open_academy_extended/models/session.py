from odoo import _, api, fields, models

class Session(models.Model):
    _inherit = "course.session"

    name = fields.Char(string="Name of the Session")
    start_datetime = fields.Datetime(required=True)
    state = fields.Selection([('new', 'New'), ('confirm', 'Confirm'), ('done', 'Done')], default="new")