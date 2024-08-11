from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('ordemsaida/', views.ordemsaida, name='saida'),
]