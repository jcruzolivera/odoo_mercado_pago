from odoo import http
from odoo.http import request
import mercadopago
import os

class PaymentController(http.Controller):

    @http.route('/payment/mercado_pago', type='json', auth='public')
    def mercado_pago_payment(self, **kwargs):
        # Obtener el token de la variable de entorno
        access_token = os.getenv('MERCADOPAGO_ACCESS_TOKEN')
        if not access_token:
            return {"error": "Access token not found"}

        # Instancia del SDK de Mercado Pago
        mp = mercadopago.SDK(access_token)

        # Crear una preferencia de pago
        preference_data = {
            "items": [
                {
                    "title": "Título del producto",
                    "quantity": 1,
                    "currency_id": "ARS",
                    "unit_price": 100.00
                }
            ],
            "payer": {
                "email": kwargs.get('email', 'default_email@example.com')
            },
            "back_urls": {
                "success": "#/success",
                "failure": "#/failure",
                "pending": "#/pending"
            },
            "auto_return": "approved",
        }

        # Crear preferencia en Mercado Pago
        preference_response = mp.preference().create(preference_data)
        preference = preference_response['response']

        # Redirigir al usuario a Mercado Pago
        return {
            "redirect_url": preference['init_point']
        }

    @http.route('/payment/mercado_pago/response', type='http', auth='public', csrf=False)
    def mercado_pago_response(self, **kwargs):
        # Lógica para manejar la respuesta de Mercado Pago después del pago
        payment_status = request.params.get('status')
        payment_id = request.params.get('payment_id')

        if payment_status == 'approved':
            # Lógica para pagos aprobados
            pass
        elif payment_status == 'pending':
            # Lógica para pagos pendientes
            pass
        elif payment_status == 'failure':
            # Lógica para pagos fallidos
            pass

        return "Payment response processed"
