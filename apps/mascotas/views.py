from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mascota
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect, Http404

class RegistrarMascota(LoginRequiredMixin, CreateView):
	model = Mascota
	fields = ('usuario','nombre','imagen','fec_nac','especie','raza','sexo','nomb_opcional','slug')

	template_name='pages/RegistroAnimalBasico.html'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		request.POST._mutable=True
		us=request.user.id
		form.data['usuario']=us
		wep=form.data['nombre']
		form.data['slug']=""+slugify(wep)+""+str(us)
		slug=form.data['slug']
		if form.is_valid():
			return self.form_valid(form,{'slug':slug})
		else:
			return self.form_invalid(form)

	def form_valid(self, form,kwargs):
		self.object = form.save()
		x=kwargs['slug']
		return HttpResponseRedirect(reverse_lazy('mascotas:agregarinfomedica',kwargs={'slug':x}))
	
	def form_invalid(self,form):
		response= HttpResponse("Parece que hubo un error al registrar su mascota.")
		response.write("<div>Intente de nuevo haciendo clic <a href=''>aquí</a></div>")
		response.write("<div>Tal vez esta mascota ya existe?</div>")
		return response

class RegistrarParte2(UpdateView):
	model = Mascota
	template_name='pages/RegistroAnimalDetallado.html'
	fields=('info_medica','nom_doc','nom_vet','dir_vet','tel_vet','cp_vet','ciudad_vet','detalles_vet')
	def get_queryset(self):
		x=self.kwargs['slug']
		context=Mascota.objects.filter(slug=x)
		return context

	def form_valid(self, form):
		self.object = form.save()
		x=self.kwargs['slug']
		return HttpResponseRedirect(reverse_lazy('mascotas:confirmar',kwargs={'slug':x}))


class ConfirmarMascota(LoginRequiredMixin, DeleteView):
	model=Mascota
	template_name='pages/RegistroAnimalConfirmacion.html'
	success_url=reverse_lazy('mascotas:nuevo')
	def get_object(self, queryset=None):
		obj = super(ConfirmarMascota, self).get_object()
		if not obj.usuario == self.request.user:
			raise Http404
		return obj
	def get_queryset(self):
		x=self.kwargs['slug']
		context=Mascota.objects.filter(slug=x)
		return context

class VerMascotas(LoginRequiredMixin,ListView):
	model = Mascota
	#template_name =
	def get_queryset(self):
		user= request.user
		context=Mascota.objects.filter(usuario_id=user)
		return context

class DetallesMascota(LoginRequiredMixin, DetailView):
	model = Mascota
	#template_name = 

class ActualizarMascota(LoginRequiredMixin, UpdateView):
	model = Mascota
	#template_name=