# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Cs_vehicle_logHrEmployee(models.Model):
    _inherit = 'hr.employee'

    preferred_vehicle = fields.Many2one('cs_vehicle_log.vehicles', "Preferred Vehicle")