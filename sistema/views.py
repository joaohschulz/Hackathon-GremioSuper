from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from sistema.models import Chamado, AdministrarChamado
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChamadoForm, AdmChamadoForm
from django.urls import reverse_lazy


# Create your views here.

class BaseView(TemplateView):
    template_name = 'conteudo_base.html'
    
class ChamadoView(LoginRequiredMixin, ListView):
    form_class = ChamadoForm
    login_url = 'login'
    context_object_name = 'chamados'    
    template_name = 'chamados.html'
    model = Chamado
    
    # contexto para pegar os chamados do usuário logado
    def get_queryset(self):
        return Chamado.objects.filter(cidadao=self.request.user)
 
class NovoChamadoView(LoginRequiredMixin, CreateView):
    form_class = ChamadoForm
    login_url = 'login'
    template_name = 'novo_chamado.html'
    model = Chamado
    success_url = reverse_lazy('chamados')
    
    def form_valid(self, form):
        form.instance.cidadao = self.request.user
        return super().form_valid(form)
    
