from django.db import models
from django.contrib.auth.models import User
from sistema.models import Orgao
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=20, choices=[('Cidadao', 'Cidadão'), ('Administrador', 'Administrador')], default='Cidadao')
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.usuario.username