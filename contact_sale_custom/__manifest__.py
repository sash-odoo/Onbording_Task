# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale and Contact Custom',
    'description': """"
                Sale Customization
                Contact Customization
                TASK - 2763183 | Version - 15.0    
    """,
    'version': '15.0.1',
    'category': 'Sales',
    'depends': ['base', 'contacts' , 'sale' , 'sale_stock' , 'stock'],
    'data': [
        'views/res_view.xml',
        'views/sale.xml',
        'views/stock.xml',
    ],
    'installable': True,
    'auto_install': False,
}
