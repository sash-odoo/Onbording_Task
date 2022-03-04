# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"

    days_to_deliver = fields.Integer(string='Days to Deliver', default='10', store=True)
    number_of_days = fields.Integer(string='Number of Days' , store=True , default='10')

    @api.constrains('days_to_deliver')
    def _check_days_to_deliver(self):
        for record in self:
            if record.days_to_deliver < 0:
                raise ValidationError("Please Enter positive value in Days to Deliver")

