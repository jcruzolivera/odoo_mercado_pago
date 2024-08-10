from odoo import models, fields, api

class PaymentTransaction(models.Model):
    _name = 'payment.transaction'
    _description = 'Payment Transaction'

    name = fields.Char('Transaction Reference', required=True)
    amount = fields.Float('Amount', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, default='draft')
    payment_method = fields.Selection([
        ('mercado_pago', 'Mercado Pago'),
    ], string='Payment Method', required=True, default='mercado_pago')
