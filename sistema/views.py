from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from sistema.models import Chamado, AdministrarChamado
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChamadoForm, AdmChamadoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404




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
    
    # aq ele seta o cidadao do chamado como o usuário logado antes de salvar
    def form_valid(self, form):
        form.instance.cidadao = self.request.user
        return super().form_valid(form)
    
    
# aq ele configura que para acessar as views de adm precisa ter o status de administrador
# o test_func verifica se o usuário logado tem o perfil de administrador, 
# se n tiver ele redireciona para a página de login   
class VerificarAdm(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'
    def test_func(self):
        perfil = getattr(self.request.user, 'perfil', None) 
        return perfil is not None and perfil.tipo_usuario == 'Administrador'
    
    
class AdmChamadoView(VerificarAdm, ListView):
    form_class = AdmChamadoForm
    login_url = 'login'
    context_object_name = 'adm_chamados'    
    template_name = 'adm_dashboard.html'
    model = AdministrarChamado
    
    # contexto para pegar os chamados do orgão do usuário logado
    def get_queryset(self):
        orgao = self.request.user.perfil.orgao
        return Chamado.objects.filter(categoria__orgao=orgao)
    
class VerChamadoView(VerificarAdm, TemplateView):
    template_name = 'ver_chamado.html'
    login_url = 'login'
    
    # isso aq basicamente serve para pegar o chamado pelo id 
    # que vem na url e passar para o contexto da página
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chamado_id = self.kwargs.get('chamado_id')
        chamado = Chamado.objects.get(id=chamado_id)
        context['chamado'] = chamado
        return context
    
class GerenciarChamadoView(VerificarAdm, CreateView):
    form_class = AdmChamadoForm
    login_url = 'login'
    template_name = 'gerenciar_chamados.html'
    model = AdministrarChamado
    success_url = reverse_lazy('adm_chamados')
    
    # isso aq basicamente serve para pegar o chamado pelo id 
    # que vem na url e passar para o contexto da página
    # se n der, ele retorna 404
    def get_chamado(self):
        return get_object_or_404(Chamado, id=self.kwargs.get('chamado_id'))
    
    # aq ele pega o status do chamado e seta no form
    # para que o admin possa ver o status atual do chamado
    def get_initial_status(self):
        chamado = self.get_chamado()
        return {'status': chamado.status, 'usuario': self.request.user}
    
    # aq o get_context_data passa o chamado para o template
    # para que ele possa ser exibido na página
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chamado'] = self.get_chamado()
        return context
    
    # aq o form_valid seta o chamado no form antes de salvar
    def form_valid(self, form):
        form.instance.chamado = self.get_chamado()
        return super().form_valid(form)