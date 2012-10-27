from maratones.models import Solicitud, Inscripcion, Patrocinante, Premiacion, CuentaBancaria, Pago
from django.contrib import admin


# Modelos registrados en el admin

admin.site.register(Solicitud)
admin.site.register(Inscripcion)
admin.site.register(Patrocinante)
admin.site.register(Premiacion)
admin.site.register(CuentaBancaria)
admin.site.register(Pago)
