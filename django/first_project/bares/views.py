from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.html import escape

BARES = [
    {"id": 1, "nombre": "Casa Felipe", "barrio": "La Viña"},
    {"id": 2, "nombre": "El Faro", "barrio": "El Pópulo"},
    {"id": 3, "nombre": "Bar Cañailla", "barrio": "La Viña"},
]

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

def inspector(request):
	return HttpResponse(
		f"method: {request.method}\n"
		f"path: {request.path}\n"
		f"GET: {dict(request.GET)}\n",
		content_type="text/plain; chaset=utf-8"
	)

def buscar(request):
    valores = request.GET.getlist("q")
    termino = valores[0].strip() if valores else ""
    if termino == "":
        return HttpResponse(
            "Escribe un término de búsqueda: /bares/buscar/?q=camarones"
        )
    aviso = ""
    if len(valores) > 1:
        aviso = "<p>El parámetro q llegó repetido; solo se atiende al primero.</p>"
    return HttpResponse(f"{aviso}<p>Buscando «{escape(termino)}»...</p>")

def detalle(request, pk):
	for bar in BARES:
		if bar.get('id') == pk:
			return HttpResponse(
				f"<h1>{bar.get('nombre')}</h1><p>Barrio: {bar.get('barrio')}</p>"
			)
		return HttpResponseNotFound("No hay ningún bar con ese ID.")
