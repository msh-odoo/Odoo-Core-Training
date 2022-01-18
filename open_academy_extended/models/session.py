from odoo import api, fields, models

class Session(models.Model):
    _inherit = "course.session"

    start_datetime = fields.Datetime(required=True)