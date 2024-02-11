# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from collections import OrderedDict
from operator import itemgetter

from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem
from odoo.osv.expression import OR, AND


class ProjectCustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        if 'issue_count' in counters:
            values['issue_count'] = request.env['sh.issue'].search_count([('sh_partner_id', '=', request.env.user.partner_id.id)]) \
                if request.env['sh.issue'].check_access_rights('read', raise_exception=False) else 0
        return values

    def _issue_get_searchbar_sortings(self):
        return {
            'date': {'label': _('Newest'), 'order': 'create_date desc', 'sequence': 1},
            'name': {'label': _('Title'), 'order': 'name', 'sequence': 2},
            'project': {'label': _('Project'), 'order': 'sh_project_id, sh_stage_id', 'sequence': 3},
            'stage': {'label': _('Stage'), 'order': 'sh_stage_id, sh_project_id', 'sequence': 4},
        }

    # ------------------------------------------------------------
    # My Issue
    # ------------------------------------------------------------
    def _issue_get_page_view_values(self, issue, access_token, **kwargs):
        page_name = 'issue'
        history = 'my_issue_history'
        try:
            issue_accessible = bool(self._document_check_access(
                'sh.issue', issue.id))
        except (AccessError, MissingError):
            issue_accessible = False
        values = {
            'page_name': page_name,
            'issue': issue,
            'user': request.env.user,
            'issue_accessible': issue_accessible,
        }
        return self._get_page_view_values(issue, access_token, values, history, False, **kwargs)

    def _issue_get_groupby_mapping(self):
        return {
            'project': 'sh_project_id',
            'stage': 'sh_stage_id',
        }

    def _issue_get_order(self, order, groupby):
        groupby_mapping = self._issue_get_groupby_mapping()
        field_name = groupby_mapping.get(groupby, '')
        if not field_name:
            return order
        return '%s, %s' % (field_name, order)

    def _issue_get_searchbar_inputs(self):
        values = {
            'all': {'input': 'all', 'label': _('Search in All'), 'order': 1},
            'ref': {'input': 'ref', 'label': _('Search in Ref'), 'order': 1},
            'project': {'input': 'project', 'label': _('Search in Project'), 'order': 2},
            'stage': {'input': 'stage', 'label': _('Search in Stages'), 'order': 3},
        }
        return dict(sorted(values.items(), key=lambda item: item[1]["order"]))

    def _issue_get_searchbar_groupby(self):
        values = {
            'none': {'input': 'none', 'label': _('None'), 'order': 1},
            'project': {'input': 'project', 'label': _('Project'), 'order': 2},
            'stage': {'input': 'stage', 'label': _('Stage'), 'order': 4},
        }
        return dict(sorted(values.items(), key=lambda item: item[1]["order"]))

    def _issue_get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('customer', 'all'):
            search_domain.append([('sh_partner_id', 'ilike', search)])
        if search_in in ('stage', 'all'):
            search_domain.append([('sh_stage_id', 'ilike', search)])
        if search_in in ('project', 'all'):
            search_domain.append([('sh_project_id', 'ilike', search)])
        if search_in in ('ref', 'all'):
            search_domain.append([('id', 'ilike', search)])
        return OR(search_domain)

    def _prepare_issues_values(self, page, date_begin, date_end, sortby, search, search_in, groupby, url="/my/issues", domain=None, su=False):
        values = self._prepare_portal_layout_values()

        Issue = request.env['sh.issue']
        searchbar_sortings = dict(sorted(self._issue_get_searchbar_sortings().items(),
                                         key=lambda item: item[1]["sequence"]))
        searchbar_inputs = self._issue_get_searchbar_inputs()
        searchbar_groupby = self._issue_get_searchbar_groupby()

        if not domain:
            domain = []
        if not su and Issue.check_access_rights('read'):
            domain = AND(
                [domain, request.env['ir.rule']._compute_domain(Issue._name, 'read')])
        Issue_sudo = Issue.sudo()

        # default sort by value
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        # default group by value
        if not groupby:
            groupby = 'project'

        # search
        if search and search_in:
            domain += self._issue_get_search_domain(search_in, search)

        # content according to pager and archive selected
        order = self._issue_get_order(order, groupby)

        def get_grouped_issues(pager_offset):
            issues = Issue_sudo.search(
                domain, order=order, limit=self._items_per_page, offset=pager_offset)
            request.session['my_issue_history'] = issues.ids[:100]

            groupby_mapping = self._issue_get_groupby_mapping()
            group = groupby_mapping.get(groupby)
            if group:
                grouped_issues = [Issue_sudo.concat(
                    *g) for k, g in groupbyelem(issues, itemgetter(group))]
            else:
                grouped_issues = [issues]

            return grouped_issues

        values.update({
            'grouped_issues': get_grouped_issues,
            'page_name': 'issue',
            'default_url': url,
            'issue_url': 'issue',
            'pager': {
                "url": url,
                "url_args": {'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby, 'groupby': groupby, 'search_in': search_in, 'search': search},
                "total": Issue_sudo.search_count(domain),
                "page": page,
                "step": self._items_per_page
            },
            'searchbar_sortings': searchbar_sortings,
            'searchbar_groupby': searchbar_groupby,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
            'sortby': sortby,
            'groupby': groupby,
        })
        return values

    def _get_my_issues_searchbar_filters(self, project_domain=None, issue_domain=None):
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
        }

        # extends filterby criteria with project the customer has access to
        projects = request.env['project.project'].search(project_domain or [])
        for project in projects:
            searchbar_filters.update({
                str(project.id): {'label': project.name, 'domain': [('sh_project_id', '=', project.id)]}
            })

        # extends filterby criteria with project (criteria name is the project id)
        # Note: portal users can't view projects they don't follow
        project_groups = request.env['project.task'].read_group(
            [('project_id', 'not in', projects.ids)], ['project_id'], ['project_id'])

        for group in project_groups:
            proj_id = group['project_id'][0] if group['project_id'] else False
            proj_name = group['project_id'][1] if group['project_id'] else _(
                'Others')
            searchbar_filters.update({
                str(proj_id): {'label': proj_name, 'domain': [('sh_project_id', '=', proj_id)]}
            })
        return searchbar_filters

    @http.route(['/my/issues', '/my/issues/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_issues(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, search=None, search_in='content', groupby=None, **kw):

        searchbar_filters = self._get_my_issues_searchbar_filters()

        if not filterby:
            filterby = 'all'
        domain = searchbar_filters.get(
            filterby, searchbar_filters.get('all'))['domain']
        domain += [('sh_partner_id', '=', request.env.user.partner_id.id)]

        values = self._prepare_issues_values(
            page, date_begin, date_end, sortby, search, search_in, groupby, domain=domain)

        # pager
        pager_vals = values['pager']
        pager_vals['url_args'].update(filterby=filterby)
        pager = portal_pager(**pager_vals)

        values.update({
            'grouped_issues': values['grouped_issues'](pager['offset']),
            'pager': pager,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
        })
        return request.render("sh_project_task_issue_management.portal_my_issues", values)

    @http.route(['/my/issue/<int:issue_id>'], type='http', auth="public", website=True)
    def portal_my_issue(self, issue_id, access_token=None, **kw):
        try:
            issue_sudo = self._document_check_access(
                'sh.issue', issue_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = self._issue_get_page_view_values(
            issue_sudo, access_token, **kw)
        return request.render("sh_project_task_issue_management.portal_my_issue", values)
