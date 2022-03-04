# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api , _


class Customer(models.Model):
    _inherit = "res.partner"

    # Create() for generate the sequence
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner.customer')
        return super().create(vals)

        vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner.vendor')
        return super().create(vals)

