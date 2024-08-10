{
    'name': 'Mercado Pago Integration',
    'version': '1.0',
    'category': 'Payment',
    'summary': 'Integrates Mercado Pago payment gateway with Odoo',
    'description': """
        This module integrates Mercado Pago with Odoo, allowing payments to be processed via Mercado Pago.
    """,
    'depends': ['base', 'payment'],
    'data': [
        'views/payment_views.xml',
    ],
    'installable': True,
    'application': True,
}
