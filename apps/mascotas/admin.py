from django.contrib import admin
from .models import Mascota
from .models import Perdidos
# Register your models here.



#registrame en el sitio del admin, mi MODELO
admin.site.register(Mascota)
admin.site.register(Perdidos)