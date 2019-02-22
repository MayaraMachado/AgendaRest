from django.contrib import admin
from django.urls import path
from .views import *
from .api import views as api

urlpatterns = [
    path('hello/', HelloView.as_view(), name="hello"),
    path('profiles/', api.ProfileList.as_view(), name="profiles"),
    path('profiles/<int:pk>/', api.ProfileDetail.as_view(), name="profiles-details"),
    path('agendamentos/', api.AgendamentoList.as_view(), name="agendamentos"),
    path('agendamentos/<int:pk>', api.AgendamentoDetail.as_view(), name="agendamentos-detalhe"),
]
