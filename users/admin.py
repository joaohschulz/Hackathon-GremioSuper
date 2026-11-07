from django.contrib import admin
from .models import Perfil
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_usuario', 'orgao')
admin.site.register(Perfil, PerfilAdmin)    