from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponse

def home(request):
    return render_to_response('maratones/home.html', {},
                               context_instance=RequestContext(request))

def ubicacion(request):
    return render_to_response('maratones/ubicacion.html', {},
                               context_instance=RequestContext(request))

def itinerario(request):
    return render_to_response('maratones/itinerario.html', {},
                               context_instance=RequestContext(request))

def inscripciones(request):
    return render_to_response('maratones/home.html', {},
                               context_instance=RequestContext(request))

def login(request):
    return render_to_response('maratones/home.html', {},
                               context_instance=RequestContext(request))