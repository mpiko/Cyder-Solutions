# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models


class SHIssueType(models.Model):
    _name = 'sh.issue.type'
    _description = "Issue Type"

    name = fields.Char(required=True)
    sh_description = fields.Text(string='Description')
