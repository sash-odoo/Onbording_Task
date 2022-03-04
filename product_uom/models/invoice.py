# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models , api

class Invoice(models.Model):
    _inherit ='account.move.line'

    # product_id the effect of onchange()
    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super()._onchange_product_id()

        for rec in self.partner_id.inventory_order_ids:
            if rec.product_id.id == self.product_id.id:
                self.product_uom_id = rec.default_uom_id.id

                break