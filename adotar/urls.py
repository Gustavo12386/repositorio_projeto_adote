from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pets, name="listar_pets"),
    path('ver_pet/<int:id>', views.ver_pet, name="ver_pet"),
    path('pedido_adocao/<int:id_pet>', views.pedido_adocao, name="pedido_adocao"),
]