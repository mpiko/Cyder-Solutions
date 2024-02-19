# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Mx_elearning_plusMx_elearning_plus(models.Model):
    _name = "mx_elearning_plus.mx_elearning_plus"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Mx_elearning_plus"

    ref = fields.Char(string='Ref Number', default='New', tracking=True)
    name = fields.Char(string='Name')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('mx_elearning_plus.sequence')
        return super(Mx_elearning_plusMx_elearning_plus, self).create(vals)
