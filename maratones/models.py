class Inscripcion(models.Model):
	equipo = models.CharField(max_length=30)
	solic_previa = models.OneToOneField(inscripcion)
	
class Patrocinante(models.Model):
	nombre = models.CharField(max_length=30)
	rif = models.CharField(max_length=20)
	logo = models.ImageField(upload_to=)
	# Se debe de poner la direccion de "upload" en el archivo settings.py

class Premiacion(models.Model):
	nombre_premio = models.CharField(max_length=30)
	posicion = models.CharField(max_length=30)
