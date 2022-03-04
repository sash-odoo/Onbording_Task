# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models , api

class SaleOrder(models.Model):
    _inherit ='sale.order.line'

    # product_id the effect of onchange()
    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        self.onchange_uom()

    # order_partner_id the effect of onchange()
    @api.onchange('order_partner_id')
    def product_id_change(self):
        res = super().product_id_change()
        self.onchange_uom()

    def onchange_uom(self):
        if self.product_id and self.order_partner_id:
            self.product_uom = self.order_partner_id.inventory_order_ids.filtered(lambda ul: ul.product_id.id == self.product_id.id).default_uom_id.id

        # for rec in self.order_partner_id.inventory_order_ids:
        #     if rec.product_id.id == self.product_id.id:
        #         self.product_uom = rec.default_uom_id.id

                #break


