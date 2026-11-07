from django.contrib import admin
from .models import Orgao, Categoria, Chamado

class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'sigla')   
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'orgao')
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'prioridade', 'data_criacao', 'endereco', 'foto')
admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Chamado, ChamadoAdmin)