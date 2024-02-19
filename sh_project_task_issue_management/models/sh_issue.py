# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models, api, _
from odoo.exceptions import AccessError


class SHIssue(models.Model):
    _name = 'sh.issue'
    _inherit = ['portal.mixin', 'utm.mixin',
                'mail.thread', 'mail.activity.mixin', ]
    _description = "Issue"

    def _default_stage_id(self):
        return self.env['sh.issue.stages'].search([], limit=1)

    name = fields.Char(tracking=True,)
    sh_company_id = fields.Many2one(
        comodel_name='res.company', string='Company', tracking=True,)
    sh_partner_id = fields.Many2one(
        comodel_name='res.partner', string='Customer', tracking=True,)
    sh_issue_type_id = fields.Many2one(
        comodel_name='sh.issue.type', string='Issue Type', tracking=True,)
    sh_user_ids = fields.Many2many(
        comodel_name='res.users', string='Assignees', tracking=True,)
    sh_project_id = fields.Many2one(
        comodel_name='project.project', string='Project', tracking=True,)
    sh_task_id = fields.Many2one(
        comodel_name='project.task', string='Task', tracking=True, domain="[('project_id', '=', sh_project_id)]",)
    sh_stage_id = fields.Many2one(
        comodel_name='sh.issue.stages', string='Stage', default=_default_stage_id, copy=False, tracking=True,)
    sh_description = fields.Html(string='Description', tracking=True,)
    sh_additional_comment = fields.Html(
        string='Additional Comment', tracking=True,)

    # For Portal
    def _compute_access_url(self):
        super(SHIssue, self)._compute_access_url()
        for issue in self:
            issue.access_url = '/my/issue/%s' % issue.id

    @api.model
    def portal_create(self, vals):
        crt = self.env['sh.issue'].sudo().create(vals)
        return crt

    def write(self, vals):
        res = super(SHIssue, self).write(vals)
        if vals.get('sh_stage_id'):
            manager_group = self.env.user.has_group(
                'sh_project_task_issue_management.issue_group_manager')
            if not manager_group:
                raise AccessError(
                    _("You Are Not Allow To Change Stage."))
            else:
                vals['sh_stage_id'] = vals.get('sh_stage_id')
        return res
