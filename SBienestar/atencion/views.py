from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Paciente, Consulta, HistoriaClinica

from .forms import PacienteForm, ConsultaForm


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
    context = {'post': False}
    if request.POST:
        cedula = request.POST.get('cc')
        try:
            paciente = Paciente.objects.get(cedula=cedula)
            context['paciente'] = paciente
            context['post'] = True
            consultas = Consulta.objects.filter(paciente=paciente)
            nConsultas = consultas.count()
            context['consultas'] = nConsultas
        except Paciente.DoesNotExist:
            context['error'] = True
    return render(request, 'paciente.html', context)


@login_required
def agregar_paciente(request):
    form = PacienteForm(
        request.POST or None
    )
    context = {}
    if request.POST:
        if form.is_valid():
            form.save()
            context['msj'] = 'Paciente registrado'
            context['flag'] = True
            return redirect('agregar_consulta', context)
    context['form'] = form
    return render(request, 'aggPaciente.html', context)

@login_required
def agregar_consulta(request):
    #id = kwargs.get('pk')
    #paciente = Paciente.objects.get(id=id)
    form = ConsultaForm(
        request.POST or None
    )
    context = {}
    #context = {
    #    'paciente': paciente
    #}
    if request.POST:
        if form.is_valid():
            form.save()
            context['flag'] = True
            return redirect('home')
    context['form'] = form
    return render(request, 'consultaP.html', context)



class BaseListViewMixin(LoginRequiredMixin, ListView):
    pass


class CitaDoctorView(BaseListViewMixin):
    model = HistoriaClinica
    template_name = 'consultas.html'
    context_object_name = 'historias_clinicas'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if hasattr(self.request.user, 'doctor'):
            user = {
                'doctor': self.request.user.doctor
            }
            queryset = self.model.objects.filter(**user)
            #queryset = self.model.filter(**user)
        return queryset
