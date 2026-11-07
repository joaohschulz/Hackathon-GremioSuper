from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Chamado, AdministrarChamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'categoria', 'prioridade', 'endereco', 'foto']
class AdmChamadoForm(forms.ModelForm):
    class Meta:
        model = AdministrarChamado
        fields = ['chamado', 'usuario', 'status']