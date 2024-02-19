# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    sh_issue_type_config_id = fields.Many2one(
        comodel_name='sh.issue.type', string='Issue Type')
