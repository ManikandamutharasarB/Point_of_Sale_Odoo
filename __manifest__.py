      # -*- coding: utf-8 -*-
{
    'name' : 'Point_of_Sale',
    'version' : '1.1',
    'summary': 'Online Point of Sale',
    'sequence': 10,
    'description': """
Online Point of Sale    """,
    'category': 'Website',
    'website': '',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/createInventoryView.xml',
        'views/history.xml',
        'views/billing.xml',
        'views/product_details.xml',
        'views/inventory.xml',
        'views/customer.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}
