
# Odoo Mercado Pago Integration

Este módulo de Odoo 17 integra la pasarela de pagos Mercado Pago con Odoo, permitiendo la gestión de pagos y transacciones a través de Mercado Pago.

## Características

- **Integración Completa**: Conecta Odoo con Mercado Pago para procesar pagos.
- **Gestión de Transacciones**: Administra las transacciones de pago desde Odoo.
- **Interfaz de Usuario**: Accede y gestiona los pagos desde una vista intuitiva en Odoo.

## Requisitos

- Odoo 17
- Python 3.12 o superior
- SDK de Mercado Pago para Python

## Instalación

1. **Descargar el Módulo**

   Clona o descarga el módulo desde el repositorio.

   ```bash
   git clone https://github.com/tu-usuario/odoo-mercado-pago.git
   ```

2. **Instalar el SDK de Mercado Pago**

   Instala el SDK de Mercado Pago en tu entorno virtual:

   ```bash
   pip install mercadopago
   ```

3. **Agregar el Módulo a Odoo**

   Copia el módulo a la carpeta de addons de Odoo. Luego, actualiza la lista de módulos en Odoo y encuentra "Mercado Pago Integration" en la lista de módulos disponibles.

   ```bash
   cp -r odoo-mercado-pago /path/to/odoo/addons/
   ```

4. **Instalar el Módulo**

   En la interfaz de Odoo, ve a `Aplicaciones`, busca "Mercado Pago Integration" y haz clic en `Instalar`.

## Configuración

1. **Configurar Mercado Pago**

   Crea una nueva configuración para Mercado Pago en Odoo:

   - Ve a `Configuración > Mercado Pago`.
   - Introduce tu `Client ID` y `Client Secret` de Mercado Pago.

2. **Crear Credenciales de Mercado Pago**

   Añade las credenciales de Mercado Pago en el archivo de configuración:

   ```python
   from mercadopago import SDK

   class MercadoPagoConfig(models.TransientModel):
       _name = 'mercado.pago.config'

       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.sdk = SDK({
               'access_token': 'YOUR_ACCESS_TOKEN',
           })
   ```

## Uso

1. **Crear Transacciones**

   Puedes crear nuevas transacciones de pago desde el menú `Pagos > Transacciones de Pago`.

2. **Procesar Pagos**

   Redirige a los usuarios a la página de pago de Mercado Pago y maneja la respuesta de Mercado Pago para actualizar el estado de la transacción en Odoo.

## Desarrollo

Para contribuir al desarrollo de este módulo:

1. **Configura tu Entorno**

   Instala las dependencias necesarias y configura un entorno virtual.

   ```bash
   pip install -r requirements.txt
   ```

2. **Realiza Cambios**

   Desarrolla nuevas características o corrige errores en tu entorno local.

3. **Enviar Pull Request**

   Crea un pull request con tus cambios en el repositorio de GitHub.

## Soporte

Si encuentras algún problema o necesitas ayuda, por favor, abre un `issue` en el repositorio de GitHub.

## Licencia

Este módulo está licenciado bajo la [MIT License](LICENSE).

---

