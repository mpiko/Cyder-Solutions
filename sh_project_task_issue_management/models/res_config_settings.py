# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import models, fields


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    sh_issue_type_config_id = fields.Many2one(
        comodel_name='sh.issue.type', related='company_id.sh_issue_type_config_id', string='Issue Type', readonly=False)
