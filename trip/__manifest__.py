{
    'name': 'Cyder Travel Log',
    'version': '1.0',
    'summary': 'Extends fleet to add travel information',
    'category': 'Productivity',
    'description': """
Extends fleet to add travel information
""",
    'website': 'www.cyder.com.au',
    'depends': ['fleet'],
    'data': [
        'views/trips.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': -101,
}
