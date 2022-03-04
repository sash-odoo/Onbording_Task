# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    inventory_order_ids = fields.One2many('inventory.order' , 'partner_id')
