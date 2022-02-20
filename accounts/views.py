from django.shortcuts import render
from django.contrib import messages

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):
    if request.method != 'post':
        return render(request, 'accounts/cadastro.html')

    nome = request.post.get('nome')
    sobrenome = request.post.get('sobrenome')
    email = request.post.get('email')
    usuario = request.post.get('usuario')
    senha = request.post.get('senha')
    senha2 = request.post.get('senha2')

    if not nome or not sobrenome or not email or not usuario \
        or not senha or not senha2:
        pass


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
