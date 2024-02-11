
from odoo import api, models, fields

class Trips(models.Model):
    _inherit = "fleet.vehicle.odometer"

    business = fields.Boolean(string="Business", default=True)
    tolls = fields.Boolean(string="Tolls")
    startread = fields.Integer('Start', group_operator="max")
    distance = fields.Integer(string="Distance", compute="_compute_distance")
    note = fields.Text(string="Notes")

    def _compute_distance(self):
        for rec in self:
            distance = rec.value - rec.startread
            rec.distance = distance
