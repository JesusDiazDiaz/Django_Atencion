from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Paciente, Doctor, Consulta, HistoriaClinica, Antecedente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ['antecedentes_paciente']


class AntecedenteForm(forms.ModelForm):
    class Meta:
        model = Antecedente
        fields = '__all__'


class DoctorForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'especialidad',
        )


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        exclude = ['paciente']


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'
