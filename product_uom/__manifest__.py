# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Product_UOM',
    'description': """"
                Partner wise Product in Sale Order
                TASK - 2763185 | Version - 15.0    
    """,
    'version': '15.0.1',
    'author': 'Odoo PS',
    'license': 'LGPL-3',
    'category': 'Customization',
    'depends': ['contacts' , 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/contact.xml',
    ],
    'installable': True,
    'auto_install': False,

}