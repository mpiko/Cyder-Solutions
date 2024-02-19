# -*- coding: utf-8 -*-
{
    'name': 'Vehicle Log',
    'version': '1.0.6',
    'category': 'Business',
    'author': 'Cyder Solutions',
    'website': 'https://www.cyder.com.au/',
    'price': '3000.0',
    'currency': 'USD',
    'sequence': -100,
    'summary': 'Vehicle Log',
    'description': """
    Track vehicle usage
    For accounting/Tax reasons or infringment notices
    """,
    'depends': ['mail', 'hr'],
    'data': [
        'security/cs_vehicle_log_groups.xml',
        'security/ir.model.access.csv',
        'data/cs_vehicle_log_sequence.xml',
        'reports/report.xml',
        'reports/vehicle_usage_report.xml',
        'reports/vehicle_trip_report.xml',
        'reports/vehicle_report.xml',
        'views/top_menu.xml',
        'views/cs_vehicle_log_view.xml',
        'views/cs_vehicle_log_vehicles_view.xml',
        'views/vehicle_history_lines_view.xml',
        'views/hr_employee_view.xml',
    ],
    'demo': [],
    #'images': ['static/description/banner.gif'],
    'application': True,
    'auto_install': False,
    'license': 'OPL-1'
}
