from django.contrib import admin
from .models import *


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):  
    list_display = ('titulo',)

