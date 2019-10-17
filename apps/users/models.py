from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=35)
	lastname = models.CharField(max_length=40)
	residence = models.CharField(max_length=40)
	email = models.EmailField()
	image = models.ImageField(null= True)
	#IMPORTANTE!!! De ser necesario agregar el parametro
	#uploadto... Ej:
	#(upload_to='niperraidea', null= True)