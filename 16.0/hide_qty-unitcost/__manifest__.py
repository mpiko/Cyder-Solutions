
{
    'name': 'Hide Quantity & Unit Price',
    'version': '16.0.1.0.2',
    'category': 'Productivity',
    'author': 'Cyder Solutions',
    'website': 'https://www.cyder.com.au/',
    'price': '30.0',
    'currency': 'USD',
    'sequence': -65,
    'summary': 'Hide Quantity and Unit Price on SO/Quote',
    'description': """
    Hide Quantity and Unit Price on SO/Quote
    """,
    'depends': ['mail', 'sale_management'],
    'data': [
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
        'reports/report_order.xml',
        'reports/report_order_online.xml',
    ],
    'demo': [],
    # 'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1'
    }
