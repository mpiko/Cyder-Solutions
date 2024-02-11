# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models, api


class SHIssueWizard(models.TransientModel):
    _name = 'sh.issue.wizard'
    _description = "Issue Wizard"

    name = fields.Char()
    sh_company_id = fields.Many2one(
        comodel_name='res.company', string='Company')
    sh_partner_id = fields.Many2one(
        comodel_name='res.partner', string='Customer')
    sh_issue_type_id = fields.Many2one(
        comodel_name='sh.issue.type', string='Issue Type')
    sh_user_ids = fields.Many2many(
        comodel_name='res.users', string='Assignees')
    sh_project_id = fields.Many2one(
        comodel_name='project.project', string='Project')
    sh_task_id = fields.Many2one(
        comodel_name='project.task', domain="[('project_id', '=', sh_project_id)]", string='Task')
    sh_description = fields.Html(string='Description')
    sh_additional_comment = fields.Html(string='Additional Comment')

    @api.model
    def default_get(self, fields_list):
        res = super(SHIssueWizard, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')
        tasks = self.env['project.task'].sudo().browse(active_id)
        if tasks.company_id:
            res.update({'sh_company_id': tasks.company_id.id})
        if tasks.partner_id:
            res.update({'sh_partner_id': tasks.partner_id.id})
        if tasks.project_id:
            res.update({'sh_project_id': tasks.project_id.id})
        if tasks.user_ids:
            res.update({'sh_user_ids': tasks.user_ids.ids})
        if tasks:
            res.update({'sh_task_id': tasks.id})
        return res

    def action_create_issue(self):
        self.env['sh.issue'].create({
            'name': self.name,
            'sh_company_id': self.sh_company_id.id,
            'sh_partner_id': self.sh_partner_id.id,
            'sh_issue_type_id': self.sh_issue_type_id.id,
            'sh_project_id': self.sh_project_id.id,
            'sh_task_id': self.sh_task_id.id,
            'sh_user_ids': self.sh_user_ids.ids,
            'sh_description': self.sh_description,
            'sh_additional_comment': self.sh_additional_comment,
        })
