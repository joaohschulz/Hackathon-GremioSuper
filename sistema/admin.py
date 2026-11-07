from django.contrib import admin
from .models import Orgao, Categoria, Chamado, AdministrarChamado

class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'sigla')   
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'orgao')
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'prioridade', 'data_criacao', 'endereco', 'foto')
class AdministrarChamadoAdmin(admin.ModelAdmin):
    list_display = ('chamado', 'usuario', 'data_atualizacao', 'status')
admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(AdministrarChamado, AdministrarChamadoAdmin)