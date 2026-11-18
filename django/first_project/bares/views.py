from django.shortcuts import render
from django.http import HttpResponse

def portada(request):
	return HttpResponse(
		"<h1>De tapeo por Cádiz</h1>"
		"<p>Guía de bares del casco antiguo. En obras.</p>"
	)

def listado(request):
	return HttpResponse("Aquí irá el listado de bares")
