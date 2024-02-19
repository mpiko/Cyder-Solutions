# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models, api


class SHIssueProjectWizard(models.TransientModel):
    _name = 'sh.issue.project.wizard'
    _description = "Issue Project Wizard"

    name = fields.Char()
    sh_company_id = fields.Many2one(
        comodel_name='res.company', string='Company')
    sh_partner_id = fields.Many2one(
        comodel_name='res.partner', string='Customer')
    sh_issue_type_id = fields.Many2one(
        comodel_name='sh.issue.type', string='Issue Type')
    sh_user_id = fields.Many2one(
        comodel_name='res.users', string='Project Manager')
    sh_project_id = fields.Many2one(
        comodel_name='project.project', string='Project')
    sh_task_id = fields.Many2one(
        comodel_name='project.task', domain="[('project_id', '=', sh_project_id)]", string='Task')
    sh_description = fields.Html(string='Description')
    sh_additional_comment = fields.Html(string='Additional Comment')

    @api.model
    def default_get(self, fields_list):
        res = super(SHIssueProjectWizard, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')
        isuue_type_id = self.env.company.sh_issue_type_config_id.id
        projects = self.env['project.project'].sudo().browse(active_id)
        if projects.company_id:
            res.update({'sh_company_id': projects.company_id.id})
        if projects.partner_id:
            res.update({'sh_partner_id': projects.partner_id.id})
        if projects.user_id:
            res.update({'sh_user_id': projects.user_id})
        if projects:
            res.update({'sh_project_id': projects.id})
        res.update({
            'sh_issue_type_id': isuue_type_id
        })
        return res

    def action_create_issue_project(self):
        self.env['sh.issue'].create({
            'name': self.name,
            'sh_company_id': self.sh_company_id.id,
            'sh_partner_id': self.sh_partner_id.id,
            'sh_issue_type_id': self.sh_issue_type_id.id,
            'sh_project_id': self.sh_project_id.id,
            'sh_task_id': self.sh_task_id.id,
            'sh_user_ids': self.sh_user_id,
            'sh_description': self.sh_description,
            'sh_additional_comment': self.sh_additional_comment,
        })
