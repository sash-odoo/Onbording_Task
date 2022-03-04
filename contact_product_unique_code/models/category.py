# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api

class Category(models.Model):
    _inherit = "product.template"

    # Recursion Function

    def get_parent_id(self , categ_id):
        if categ_id and categ_id.sequence_id.id:
            return categ_id.sequence_id
        elif categ_id.parent_id :
            return self.get_parent_id(categ_id.parent_id)
        else:
            return False

    # Onchange on 'categ_id'

    @api.onchange('categ_id')
    def onchange_product(self):
        if self.categ_id and self.categ_id.sequence_id:
            self.default_code = self.categ_id.sequence_id.next_by_id()
        else:
            seq = self.get_parent_id(self.categ_id.parent_id)
            self.default_code = seq.next_by_id() if seq else False

