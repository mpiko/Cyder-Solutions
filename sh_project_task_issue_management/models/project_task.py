# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models


class SHTask(models.Model):
    _inherit = 'project.task'

    def _compute_issue_count(self):
        for record in self:
            record.sh_issue_count = self.env['sh.issue'].search_count(
                [('sh_task_id', '=', self.id)])

    def _compute_task_issue_count(self):
        for record in self:
            record.sh_task_issue_count = self.env['sh.issue'].search_count(
                [('sh_task_id', '=', record.id)])

    sh_issue_count = fields.Integer(
        string="Issue Count", compute='_compute_issue_count',)

    sh_task_issue_count = fields.Integer(
        string="Issue Count",
        compute='_compute_task_issue_count',
    )

    def get_issues(self):
        self.ensure_one()
        issues = self.env['sh.issue'].sudo().search([
            ('sh_task_id', 'in', self.ids)
        ])
        action = self.env["ir.actions.actions"]._for_xml_id(
            "sh_project_task_issue_management.sh_issue_action")
        if len(issues) > 1:
            action['domain'] = [('id', 'in', issues.ids)]
        elif len(issues) == 1:
            form_view = [(self.env.ref(
                'sh_project_task_issue_management.sh_issue_view_form').id, 'form')
            ]
            if 'views' in action:
                action['views'] = form_view + \
                    [(state, view)
                     for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = issues.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
