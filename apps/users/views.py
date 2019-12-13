from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# Create your views here.

from .models import CustomUser
from .forms import CustomUserCreationForm

class Registrarte(CreateView):
	model = CustomUser
	form_class=CustomUserCreationForm
	template_name='pages/RegistroPersona.html'
	success_url = reverse_lazy('mascotas:nuevo')
	def form_invalid(self, form):
		response= HttpResponse("Error, usuario ya existente")
		response= HttpResponse("O error al ingresar la contraseña")
		response= HttpResponse("O cayó un meteorito y destruyó el server")
		response= HttpResponse("No sé, hay un error")
		response.write("<a href=''>Volver</a>")
		return response