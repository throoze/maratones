from django.db import models

class CuentaBancaria(models.Model):
    banco = models.CharField(max_length=30)
    cta = models.IntegerField()
    tipo_cta = models.CharField(max_length=10)
    titular = models.CharField(max_length=30)

class Solicitud(models.Model):
    nombre_del_coach = models.CharField(max_length=50)
    nombre_del_participante_1 = models.CharField(max_length=50)
    nombre_del_participante_2 = models.CharField(max_length=50)
    nombre_del_participante_3 = models.CharField(max_length=50)
    cedula_del_coach = models.CharField(max_length=50)
    cedula_del_participante_1 = models.CharField(max_length=50)
    cedula_del_participante_2 = models.CharField(max_length=50)
    cedula_del_participante_3 = models.CharField(max_length=50)
    email_del_coach = models.CharField(max_length=50)
    email_del_participante_1 = models.CharField(max_length=50)
    email_del_participante_2 = models.CharField(max_length=50)
    email_del_participante_3 = models.CharField(max_length=50)

class Pago(models.Model):
    num_ref = models.CharField(max_length=50)
    monto = models.IntegerField()
    solicitud = models.ForeignKey(Solicitud)
    cta = models.ForeignKey(CuentaBancaria)

class Inscripcion(models.Model):
    equipo = models.CharField(max_length=30)
    solic_previa = models.OneToOneField(Solicitud)

class Patrocinante(models.Model):
    nombre = models.CharField(max_length=30)
    rif = models.CharField(max_length=20)
#    logo = models.ImageField(upload_to=)
# Se debe de poner la direccion de "upload" en el archivo settings.py

class Premiacion(models.Model):
    nombre_premio = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
