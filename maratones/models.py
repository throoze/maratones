from django.db import models

class CuentaBancaria(models.Model):
    banco = models.CharField(max_length=30)
    cta = models.FieldInteger()
    tipo_cta = models.CharField(max_length=10)
    titular = models.CharField(max_length=30)


class Solicitud(models.Model):

    coach = models.CharField(max_length=30)
    participante = models.CharField(max_length=30)
    participante2 = models.CharField(max_length=30)
    participante3 = models.CharField(max_length=30)
    forma_pago = models.CharField(max_length=30)


class Pago(models.Model):
    num_ref = models.CharField(max_length=50)
    monto = models.IntegerField()
    solicitud = models.ForeignKey(models.Solicitud)
    cta = models.ForeignKey(models.CuentaBancaria)

    



    
