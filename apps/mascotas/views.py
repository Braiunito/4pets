from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mascota, Perdidos
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

class MascotaPerdida(LoginRequiredMixin, CreateView):
	model= Perdidos
	fields=('mascota','a','b','c','d','e')
	template_name='pages/testing.html'



	def post(self, request, *args, **kwargs):
		form = self.get_form()
		request.POST._mutable=True
		x=kwargs['slug']
		r=Mascota.objects.filter(slug=x)
		form.data['mascota']=r[0].id
		form.data['e']=True
		if form.is_valid():
			return self.form_valid(form)
		else:
			print(form.cleaned_data['a'])

			print(form.cleaned_data['c'])
			print(form.cleaned_data['d'])
			print(form.cleaned_data['e'])

			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(reverse_lazy('mascotas:mismascotas'))
	
	def form_invalid(self,form):
		response= HttpResponse("Algo salió mal, bastante mal diria yo")
		response.write("<div>Intente de nuevo haciendo clic <a href=''>aquí</a></div>")
		return response


class RegistrarParte2(LoginRequiredMixin, UpdateView):
	model = Mascota
	template_name='pages/RegistroAnimalDetallado.html'
	fields=('info_medica','nom_doc','nom_vet','dir_vet','tel_vet','cp_vet','ciudad_vet','detalles_vet')
	def get_queryset(self):
		x=self.kwargs['slug']
		context=Mascota.objects.filter(slug=x)
		return context
	def get_object(self, queryset=None):
		obj = super(RegistrarParte2, self).get_object()
		if not obj.usuario == self.request.user:
			raise Http404
		return obj
	def form_valid(self, form):
		self.object = form.save()
		x=self.kwargs['slug']
		return HttpResponseRedirect(reverse_lazy('mascotas:confirmar',kwargs={'slug':x}))
	def form_invalid(self,form):
		response= HttpResponse("Algo pasó")
		response.write("<div>Intente de nuevo haciendo clic <a href=''>aquí</a></div>")
		return response

class ConfirmarMascota(LoginRequiredMixin, DeleteView):
	model=Mascota
	template_name='pages/RegistroAnimalConfirmacion.html'
	success_url=reverse_lazy('mascotas:mismascotas')
	def get_object(self, queryset=None):
		obj = super(ConfirmarMascota, self).get_object()
		if not obj.usuario == self.request.user:
			raise Http404
		return obj
	def get_queryset(self):
		x=self.kwargs['slug']
		context=Mascota.objects.filter(slug=x)
		return context

class MisMascotas(LoginRequiredMixin,ListView):
	model = Mascota
	template_name ='pages/MisMascotas.html'
	def get_queryset(self):
		request=self.request
		user= request.user.pk
		queryset=Mascota.objects.filter(usuario_id=user)
		return queryset


class DetallesMascota(LoginRequiredMixin, DetailView):
	model = Mascota
	template_name ='Pages/PerfilMascota.html'
	def get_queryset(self):
		this= self.kwargs['slug']
		queryset=Mascota.objects.filter(slug=this)
		return queryset

class ActualizarMascota(LoginRequiredMixin, UpdateView):
	model = Mascota
	#template_name=