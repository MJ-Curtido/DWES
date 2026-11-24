from django.shortcuts import render
from django.http import HttpResponse

def portada(request):
	return HttpResponse(
		"<h1>De tapeo por Cádiz</h1>"
		"<p>Guía de bares del casco antiguo. En obras.</p>"
	)

def listado(request):
	return HttpResponse("Aquí irá el listado de bares")
	# return HttpResponse("<h2>Prueba</h2>Aquí irá el listado de bares", content_type="text/plain; charset=utf-8")

def info(request):
	return HttpResponse(
		"<p>Esta guía está escrita por Manuel Jesús Curtido Rosado en Python con Django</p>"
	)
