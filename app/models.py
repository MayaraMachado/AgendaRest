from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Agendamento(models.Model):
    criador = models.ForeignKey(User, verbose_name="Criador", on_delete=models.CASCADE)
    titulo = models.CharField("Título", max_length=200)
    local = models.CharField("Local", max_length=300)
    descricao = models.TextField("Descrição")
    data = models.DateField("Data")
    hora = models.TimeField("Hora")
    publico = models.BooleanField("Público?")
    convidados = models.ManyToManyField(User, related_name="convidados", blank=True)
    visivel = models.BooleanField(default= True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"

class UserB(User):
    class Meta:
        verbose_name="User B"
