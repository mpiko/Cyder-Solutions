
from odoo import api, models, fields

class Trips(models.Model):
    _inherit = "fleet.vehicle.odometer"

    # purpose = fields.Selection([
    #     ('private', "Private"),
    #     ('meeting', 'Meeting'),
    #     ('onsite', 'On-Site'),
    #     ('demo', 'Demonstration'),
    #     ('train', 'Training')
    # ], required=True, default='meeting')
    business = fields.Boolean(string="Business")
    tolls = fields.Boolean(string="Tolls")
    startread = fields.Integer('Start', group_operator="max")
    distance = fields.Integer(string="Distance", compute="_compute_distance")
    note = fields.Text(string="Notes")

    def _compute_distance(self):
        for rec in self:
            distance = rec.value - rec.startread
            rec.distance = distance

class TripsLog(models.Model):
    _name = "fleet.vehicle.log"
    _description = "Trip log"
    _order = 'startdate desc'

    startdate = fields.Datetime(string="Start", default=fields.Date.context_today)
    enddate = fields.Datetime(string="End", default=fields.Date.context_today)
    purpose = fields.Boolean(string="Business")
    tolls = fields.Boolean(string="Tolls")
    note = fields.Text(string="Notes")
    # name = fields.Char(compute='_compute_vehicle_log_name', store=True)
    value = fields.Float('Odometer Value', group_operator="max")
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle', required=True)
    unit = fields.Selection(related='vehicle_id.odometer_unit', string="Unit", readonly=True)
    driver_id = fields.Many2one(related="vehicle_id.driver_id", string="Driver", readonly=False)

    # @api.depends('vehicle_id', 'startdate')
    # def _compute_vehicle_log_name(self):
    #     for record in self:
    #         name = record.vehicle_id.name
    #         if not name:
    #             name = str(record.startdate)
    #         elif record.startdate:
    #             name += ' / ' + str(record.startdate)
    #         record.name = name
    #
    # @api.onchange('vehicle_id')
    # def _onchange_vehicle(self):
    #     if self.vehicle_id:
    #         self.value = self.vehicle_id.id
