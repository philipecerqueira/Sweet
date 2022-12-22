from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar_vendedor/', views.addSeller, name='addSeller'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete_account/<str:id>/', views.deleteAccount, name='deleteAccount'),
]
