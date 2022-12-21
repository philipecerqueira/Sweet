from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar_vendedor/', views.addSeller, name='addSeller'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
