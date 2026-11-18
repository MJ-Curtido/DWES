from django.urls import path
from bares import views

""" Aquí se pone la ruta a la que se accede, con su función en views que queremos que ejecute """
urlpatterns = [
	path("", views.portada, name="portada"),
	path("bares/", views.listado, name="listado"),
]
