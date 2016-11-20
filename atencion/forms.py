from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Paciente, Doctor, Consulta, ExamenFisico, Antecedente, Facultad, Enfermedad,Departamento, Eps


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class MultiConsulta(forms.Form):
    facultad = forms.ModelChoiceField(
        queryset=Facultad.objects.all(),
        empty_label='Sin Seleccionar',
        required=False
    )
    motivo = forms.ModelChoiceField(
        queryset=Enfermedad.objects.all(),
        empty_label='Sin Seleccionar',
        required=False
    )
    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        empty_label='Sin Seleccionar',
        required=False
    )
    eps = forms.ModelChoiceField(
        queryset=Eps.objects.all(),
        empty_label='Sin Seleccionar',
        required=False
    )
    fecha_inicial = forms.DateField(required=False)
    fecha_final = forms.DateField(required=False)


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

