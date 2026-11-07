from django.contrib import admin
from django.urls import path
from .views import BaseView, ChamadoView, NovoChamadoView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('chamados/', ChamadoView.as_view(), name='chamados'),
    path('chamados/novo/', NovoChamadoView.as_view(), name='novo_chamado'),
]
