# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Custom',
    'description': """"
                Sale Customization
                TASK - 2763184 | Version - 15.0    
    """,
    'version': '15.0.1',
    'author': 'Odoo PS',
    'license': 'LGPL-3',
    'category': 'Customization',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,

}
