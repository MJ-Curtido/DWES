from django.urls import path
from bares import views

""" Aquí se pone la ruta a la que se accede, con su función en views que queremos que ejecute """
urlpatterns = [
	path("", views.portada, name="portada"),
	# En la ruta bares (sin barra final), te devuelve un código de estado 301 Moved Permanently, y Location a /bares/, que lo hace internamente Django
	path("<int:pk>/", views.detalle, name="detalle"),
	path("buscar/", views.buscar, name="buscar"),
]
