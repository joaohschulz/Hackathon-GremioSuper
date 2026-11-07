from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User

class Orgao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    orgao = models.ForeignKey(
        Orgao, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self):
        return self.nome


class Chamado(models.Model):
    class Prioridade(models.TextChoices):
        BAIXA = 'Baixa', 'Baixa'
        MEDIA = 'Média', 'Média'
        ALTA = 'Alta', 'Alta'  
    cidadao = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='chamados')
    prioridade = models.CharField(max_length=10, choices=Prioridade.choices, default=Prioridade.MEDIA)
    data_criacao = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotos_chamados/', blank=True, null=True)
    
    class Meta:
        ordering = ['-data_criacao']    
        
    def __str__(self):
        return self.titulo

class AdministrarChamado(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name='administracao')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'perfil__tipo_usuario': 'Administrador'})
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('Aberto', 'Aberto'), ('Em andamento', 'Em andamento'), ('Concluído', 'Concluído')], default='Aberto')

    class Meta:
        ordering = ['-data_atualizacao']

    def __str__(self):
        return f"{self.chamado.titulo} - {self.usuario.username} - {self.status}"