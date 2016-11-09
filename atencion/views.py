from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib import messages
from .models import Paciente, Consulta, Doctor, ExamenFisico
from .forms import PacienteForm, ConsultaForm, ExamenForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Q
from datetime import date


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
    context = {'flag': False}
    if request.POST:
        fechaInicial = request.POST.get('fecha_inicial')
        fechaFinal = request.POST.get('fecha_final')
        if fechaFinal is not "" and fechaInicial is not "":
            print("fecha final {0} y fecha inicial {1}".format(fechaFinal, fechaInicial))
            consultas = Consulta.objects.filter(
                Q(fecha__gte=fechaInicial) & Q(fecha__lte=fechaFinal)
            ).order_by('fecha')
            if len(consultas) > 0:
                context['consultas'] = consultas
                context['flag'] = True
    return render(request, 'home.html', context)


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
        except Paciente.DoesNotExist:
            context['error'] = True
        else:
            context['consultas'] = Consulta.objects.filter(paciente=paciente).count()
            context['paciente'] = paciente
            context['post'] = True
    return render(request, 'paciente.html', context)


@login_required
def agregar_paciente(request):
    form = PacienteForm(
        request.POST or None
    )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('ver_paciente')
    return render(request, 'aggPaciente.html', {'form': form})


@login_required
def modificar_paciente(request, **kwargs):
    id = kwargs.get('pk')
    paciente = Paciente.objects.get(id=id)
    form = PacienteForm(
        request.POST or None,
        instance=paciente
    )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('buscar_paciente')
    return render(request, 'aggPaciente.html', {'form': form})


@login_required
def eliminar_paciente(request, **kwargs):
    Paciente.objects.get(id=kwargs.get('pk')).delete()
    consultas = Consulta.objects.filter(paciente_id=kwargs.get('pk'))
    for c in consultas:
        ExamenFisico.objects.get(c.id).delete()
    consultas.delete()
    return redirect('buscar_paciente')


@login_required
def agregar_consulta(request, **kwargs):
    form = ConsultaForm(
        request.POST or None,
        pk=kwargs.get('pk'),
        doc=request.user.doctor,
    )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('ultima_consulta')
    return render(request, 'consultaP.html', {'form': form})


@login_required
def modificar_consulta(request, **kwargs):
    consulta = Consulta.objects.get(id=kwargs.get('pk'))
    form = ConsultaForm(
        request.POST or None,
        instance=consulta,
        pk=consulta.paciente_id,
        doc=consulta.doctor
    )
    if request.POST and form.is_valid():
        form.save()
        return redirect('buscar_paciente')
    return render(request, 'consultaP.html', {'form': form})


@login_required
def eliminar_consulta(request, **kwargs):
    consulta = Consulta.objects.get(id=kwargs.get('pk'))
    consulta.delete()
    return redirect('buscar_paciente')


@login_required
def agregar_examen(request, **kwargs):
    form = ExamenForm(
        request.POST or None,
        pk=kwargs.get('pk')
    )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('guardar_examen')
    return render(request, 'examen.html', {'form': form})


@login_required
def modificar_examen(request, **kwargs):
    examen = ExamenFisico.objects.get(id=kwargs.get('pk'))
    form = ExamenForm(
        request.POST or None,
        instance=examen,
        pk=examen.consulta_id
    )
    if request.POST and form.is_valid():
        form.save()
        return redirect('guardar_examen')
    return render(request, 'examen.html', {'form': form})


class BaseListViewMixin(LoginRequiredMixin, ListView):
    pass


class CitaDoctorView(BaseListViewMixin):
    model = Consulta
    template_name = 'consultas.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if hasattr(self.request.user, 'doctor'):
            user = {
                'doctor': self.request.user.doctor
            }
            queryset = self.model.objects.filter(**user)
        return queryset


class VerPacientes(BaseListViewMixin):
    model = Paciente
    template_name = 'listaPaciente.html'
    context_object_name = 'paciente'

    def get_queryset(self):
        return self.model.objects.order_by('-id')[0]


class UltimaConsulta(BaseListViewMixin):
    model = Consulta
    template_name = 'listaConsulta.html'
    context_object_name = 'consulta'

    def get_queryset(self):
        return self.model.objects.order_by('-id')[0]


class VerConsultas(BaseListViewMixin):
    model = Consulta
    template_name = 'verConsultas.html'

    def get_context_data(self, **kwargs):
        paciente = Paciente.objects.get(id=self.kwargs['pk'])
        context = super(VerConsultas, self).get_context_data(**kwargs)
        context['paciente'] = paciente
        context['consultas'] = self.model.objects.filter(paciente_id=self.kwargs['pk'])
        return context


@login_required
def historia_clinica(request, **kwargs):
    paciente = Paciente.objects.get(id=kwargs.get('pk'))
    consultas = Consulta.objects.filter(paciente_id=kwargs.get('pk'))
    context = {
        'paciente': paciente,
        'consultas': consultas
    }
    return render(request, 'historiaClinica.html', context)


@login_required
def ver_examen(request, **kwargs):
    context = {
        'consulta': Consulta.objects.get(id=kwargs.get('pk'))
    }
    try:
        examen = ExamenFisico.objects.get(consulta_id=kwargs.get('pk'))
    except ExamenFisico.DoesNotExist:
        context['post'] = False
    else:
        context['post'] = True
        context['examen'] = examen
    return render(request, 'verExamen.html', context)


class GuardarExamen(BaseListViewMixin):
    model = ExamenFisico
    template_name = 'GuardadoExamen.html'
    context_object_name = 'examen'

    def get_queryset(self):
        return self.model.objects.order_by('-id')[0]
