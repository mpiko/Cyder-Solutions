# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Project Task Issue Tracking",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "17.0.2",
    "license": "OPL-1",
    "category": "Project",
    "summary": "Project Task Bug Tracking System Project Bug Tracking System For Project Task Track Bug From Project Task Project Bug Tracking System Project Issue Tracking Projects Issue Tracking Manage Project Bug Manage Task Bug Manage Project Issue Odoo",
    "description":  """This module is beneficial for managing project task issues. Using this module, You can easily manage projects and tasks bugs/issues. You can create issues with their types and can choose a specific project and view all its tasks and issues inside the project or tasks. Also, portal users can view and create issues on their portal. You can add a description and also add comments in the issue.""",
    "depends": ['project', 'utm'],
    "data": [
            'security/sh_issue_groups.xml',
            'security/sh_issue_security.xml',
            'security/ir.model.access.csv',
            'wizard/sh_issue_wizard_views.xml',
            'wizard/sh_issue_project_wizard_views.xml',
            'views/sh_issue_type_views.xml',
            'views/sh_issue_stages_views.xml',
            'views/project_task_views.xml',
            'views/project_project_views.xml',
            'views/sh_issue_views.xml',
            'views/sh_issue_templates.xml',
            'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.css',
            'sh_project_task_issue_management/static/src/js/sh_issue.js',
            'sh_project_task_issue_management/static/src/js/summernote.js',
            # 'https://code.jquery.com/jquery-3.5.1.min.js',
            # 'https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js',
            'sh_project_task_issue_management/static/src/xml/*',
        ],
    },
    "application": True,
    "auto_install": False,
    "installable": True,
    "images": ["static/description/background.png", ],
    "price": "30",
    "currency": "EUR"
}
