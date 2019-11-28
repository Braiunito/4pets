from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404

class Home(TemplateView):
	template_name='HomePage.html'

def handler404(request, exception, template_name='404.html'):
	print(request)
	print(template_name)
	response = render(request, template_name)
	print('eo')
	response.status_code = 404
	print('wena')
	return response
