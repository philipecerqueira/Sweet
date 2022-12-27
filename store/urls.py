from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar_produto/', views.addProducts, name='addProducts'),
]
