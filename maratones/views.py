#  -*- coding: utf-8 -*-
from models import *
from forms import *
from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.http import HttpResponse

def home(request):
    return render_to_response('maratones/home.html')

def ubicacion(request):
    return render_to_response('maratones/ubicacion.html')

def itinerario(request):
    return render_to_response('maratones/itinerario.html')

def inscripcion(request):
    form = SolicitudForm()
    if request.method == 'POST':
        if form.is_valid():
            return render_to_response(
                'maratones/inscripcion.html',
                { 'form' : form,
                  'msg'  : "Agregado con éxito!"},
                context_instance=RequestContext(request))
    return render_to_response('maratones/inscripcion.html',
                              { 'form' : form,
                                'msg'  : 'Esta es la normal'},
                               context_instance=RequestContext(request))

def login(request):
    return render_to_response('maratones/home.html', {},
                               context_instance=RequestContext(request))
# def registrar(request):
#     s = Solicitud()
#     s.coach = request.POST['coach']
#     s.participante = request.POST['participante']
#     s.participante2 = request.POST['participante2']
#     s.participante3 = request.POST['participante3']
#     s.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return render_to_response('maratones/solicitud.html',{},context_instance=RequestContext(request))

# def registrar(request):
#     formset = SolicitudForm(request.POST)
#     if formset.is_valid():
#         formset.save()

#     return render_to_response('maratones/solicitud.html',{fm:formset},context_instance=RequestContext(request))


# def solicitud(request):
#     fm = SolicitudForm(request.POST)
#     if fm.is_valid():
#         fm.save()
#     return render_to_response('maratones/solicitud.html',{fm:fm},context_instance=RequestContext(request))
