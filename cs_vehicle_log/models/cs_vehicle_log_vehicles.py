# -*- coding: utf-8 -*-
from odoo import api, fields, models
class Cs_vehicle_logVehicles(models.Model):
    _name = "cs_vehicle_log.vehicles"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Vehicle log - Vehicles"

    name = fields.Char('Registration')
    veh_make = fields.Char('Make')
    veh_model = fields.Char('Model')
    veh_capacity = fields.Char('Engine Capacity')
    # sofy_od_readings = fields....
    veh_last_reading = fields.Integer("Last Reading")
    active = fields.Boolean(default=True)
    vehicle_history_line_ids = fields.One2many('vehicle.history.lines', 'task_id')

