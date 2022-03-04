# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class InventoryOrder(models.Model):
    _name = "inventory.order"

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.template', string='Product')
    default_uom_id = fields.Many2one('uom.uom' , string='UOM' , domain="[('category_id','=', uom_category_id)]")
    uom_category_id = fields.Many2one(related="product_id.uom_id.category_id")






