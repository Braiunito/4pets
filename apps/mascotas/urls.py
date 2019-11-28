from django.urls import path
from . import views

app_name = "mascotas"

urlpatterns = [
	path("nuevo/", views.RegistrarMascota.as_view(), name="nuevo"), 

	path("nuevo/<slug:slug>", views.RegistrarParte2.as_view(),name="agregarinfomedica"), 

	path("confirmar/<slug:slug>", views.ConfirmarMascota.as_view(), name="confirmar"),

	path("mismascotas/", views.MisMascotas.as_view(), name="mismascotas"),

	path("detalle/<slug:slug>", views.DetallesMascota.as_view(), name="detalle"),
]
