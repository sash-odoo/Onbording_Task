# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contact and Product Unique Code',
    'description': """"
                Contact and Product Unique Code
                TASK - 2763189 | Version - 15.0    
    """,
    'version': '15.0.1',
    'category': 'Sales',
    'depends': ['base' , 'stock'],
    'data': [
        'views/customer_sequence.xml',
        'views/product.xml',
    ],
    'installable': True,
    'auto_install': False,
}
