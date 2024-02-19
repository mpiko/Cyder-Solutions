# -*- coding: utf-8 -*-
from odoo import api, fields, models
class Mx_elearning_plusCategory(models.Model):
    _name = "mx_elearning_plus.category"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Mx_elearning_plus Category"

    name = fields.Char('Category Name')
    active = fields.Boolean(default=True)
