# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
import datetime

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    appointment_date = fields.Datetime(string='Appointment Date', readonly=False , store=True , copy=False)

    @api.depends('appointment_date' , 'partner_id')
    def _compute_scheduled_date(self):
        for record in self:
            if record.appointment_date and record.partner_id.number_of_days :
                record.scheduled_date = record.appointment_date - datetime.timedelta(days=record.partner_id.number_of_days)
            else:
                record.appointment_date = record.sale_id.appointment_date
