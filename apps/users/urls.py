from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
	path("nuevo/", views.Registrarte.as_view(), name="nuevouser"), 
]
