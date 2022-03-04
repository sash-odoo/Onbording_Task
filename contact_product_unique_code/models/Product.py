# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Product(models.Model):
    _inherit = "product.category"

    assign_sequence = fields.Boolean(string='Assign sequence')

    sequence_id = fields.Many2one("ir.sequence", string='Main Sequence', required=True )

    # onchange on 'assign_sequence'

    @api.onchange('assign_sequence')
    def onchange_assign_checked(self):
        if self.assign_sequence:
            self.sequence_id = True
        else:
            self.sequence_id = False


