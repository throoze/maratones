from maratones.models import Solicitud, Inscripcion, Patrocinante, Premiacion, CuentaBancaria, Pago
from django.contrib import admin

admin.site.register(Solicitud, Inscripcion, Patrocinante, Premiacion, CuentaBancaria, Pago)
