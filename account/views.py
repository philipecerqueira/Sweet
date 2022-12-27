from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator

from .models import Account


@has_permission_decorator('addSeller')
def addSeller(request):
    if request.method == 'GET':
        seller = Account.objects.filter(job="V")
        return render(request, 'addSeller.html', {"vendedores": seller})

    elif request.method == 'POST':
        #TODO: validar dados
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Account.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do django
            return HttpResponse('Email já existe')

        # TODO: Depois permitir o login tanto com email tanto com username
        user = Account.objects.create_user(
            first_name=name,
            last_name=lastName,
            username=email,
            email=email,
            password=password,
            job="V"
        )

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

@has_permission_decorator('deleteAccount')
def deleteAccount(request, id):
    seller = get_object_or_404(Account, id=id)
    seller.delete()
    messages.add_message(request, messages.SUCCESS, 'Conta deletada com sucesso')
    return redirect(reverse('addSeller'))

