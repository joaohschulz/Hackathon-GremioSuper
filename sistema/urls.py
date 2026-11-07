from django.contrib import admin
from django.urls import path
from .views import BaseView, ChamadoView, NovoChamadoView, AdmChamadoView, VerChamadoView, GerenciarChamadoView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('chamados/', ChamadoView.as_view(), name='chamados'),
    path('chamados/novo/', NovoChamadoView.as_view(), name='novo_chamado'),
    path('adm_chamados/', AdmChamadoView.as_view(), name='adm_chamados'),
    path('adm_chamados/<int:chamado_id>/', VerChamadoView.as_view(), name='ver_chamado'),
    path('adm_chamados/<int:chamado_id>/gerenciar/', GerenciarChamadoView.as_view(), name='gerenciar_chamado'),
]
