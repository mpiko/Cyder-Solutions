# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models


class SHIssueStages(models.Model):
    _name = 'sh.issue.stages'
    _description = "Issue Stage"

    name = fields.Char(required=True)
