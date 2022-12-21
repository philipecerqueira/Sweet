from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator

from .models import Account


@has_permission_decorator('addSeller')
def addSeller(request):
    if request.method == 'GET':
        return render(request, 'addSeller.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Account.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do django
            return HttpResponse('Email já existe')

        # TODO: Depois permitir o login tanto com email tanto com username
        user = Account.objects.create_user(username=email, email=email, password=password, job="V")

        # TODO: Redirecionar com uma mensagem
        return HttpResponse('Conta criada')

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('dashboard'))
        return render(request, 'login.html')

    elif request.method == 'POST':
        login = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=login, password=password)

        if not user:
            # TODO: Redirecionar com messagem de erro
            return HttpResponse('Email já existe')
        
        auth.login(request, user)
        return HttpResponse('Usuario logado com sucesso')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


