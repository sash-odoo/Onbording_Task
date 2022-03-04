# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
import datetime

class SaleOrder(models.Model):
    _inherit = "sale.order"

    appointment_date = fields.Datetime(string='Appointment Date', copy=False)
    commitment_date = fields.Datetime('Delivery Date', copy=False, store=True,
                                      states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
                                      compute='_compute_commitment_date')

    @api.depends('appointment_date')
    def _compute_commitment_date(self):
        for record in self:
            if record.appointment_date and record.partner_shipping_id.days_to_deliver:
                record.commitment_date = record.appointment_date - datetime.timedelta(days=record.partner_shipping_id.days_to_deliver)
            elif not record.appointment_date:
                record.commitment_date = record.commitment_date
            elif record.partner_shipping_id.days_to_deliver == 0:
                record.commitment_date = record.commitment_date
            else:
                record.commitment_date = record.commitment_date
