from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Paciente, Doctor, Consulta, ExamenFisico, Antecedente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class AntecedenteForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=[],
        empty_label=None
    )

    class Meta:
        model = Antecedente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        paciente = kwargs.pop('paciente', None)
        super().__init__(*args, **kwargs)
        self.fields['paciente'].queryset = Paciente.objects.filter(id=paciente)


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
    paciente = forms.ModelChoiceField(
        queryset=[],
        empty_label=None
    )

    doctor = forms.ModelChoiceField(
        queryset=[],
        empty_label=None
    )
    
    class Meta:
        model = Consulta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        paciente = kwargs.pop('pk', None)
        doctor = kwargs.pop('doc', None)
        consulta = kwargs.pop('consulta', None)
        super().__init__(*args, **kwargs)
        self.fields['paciente'].queryset = Paciente.objects.filter(id=paciente)
        self.fields['doctor'].queryset = Doctor.objects.filter(username=doctor)
        if consulta:
            self.fields['paciente'].queryset = Paciente.objects.filter(
                paciente=consulta.paciente
            )
            self.fields['doctor'].queryset = Doctor.objects.filter(
                username=doctor
            )
        

class ExamenForm(forms.ModelForm):
    consulta = forms.ModelChoiceField(
        queryset=[],
        empty_label=None
    )

    class Meta:
        model = ExamenFisico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        consulta = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)
        self.fields['consulta'].queryset = Consulta.objects.filter(id=consulta)

