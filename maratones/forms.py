from django import forms
from django.db import models
from models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
