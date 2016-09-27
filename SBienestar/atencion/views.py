from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Paciente


# Create your views here.

def log_in(request):
    context = {'panel': False}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                context = {'msj': 'El usuario ha sido desactivado', 'panel': True}
        else:
            context = {'msj': 'Usuario o Contraseña incorrecta', 'panel': True}

    return render(request, 'login.html', context)


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def log_out(request):
    logout(request)
    return redirect('log_in')


@login_required
def busqueda_paciente(request):
    context = {'post': False }
    if request.POST:
        cedula = request.POST.get('cedula')
        try:
            paciente = Paciente.objects.get(cedula=cedula)
            context['paciente'] = paciente
            context['post'] = True
        except Paciente.DoesNotExist:
            context['error'] = True
    return render(request, 'paciente.html', context)


@login_required
def agregar_consulta(request):
    pass
