"""SBienestar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, includes
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from atencion import views
from django.conf.urls import url, handler404
from django.contrib import admin
from atencion.views import error_404

handler404 = '404.html'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.log_in, name='log_in'),
    url(r'^home/', views.home, name='home'),
    url(r'^logout/', views.log_out, name='log_out'),
    url(r'^agregar-paciente', views.agregar_paciente, name='agregar_paciente'),
    url(r'^modificar-paciente/(?P<pk>\w+)/', views.modificar_paciente, name='modificar_paciente'),
    url(r'^eliminar-paciente/(?P<pk>\w+)/', views.eliminar_paciente, name='eliminar_paciente'),
    url(r'^buscar-paciente/', views.busqueda_paciente, name='buscar_paciente'),
    url(r'^consultas/', views.CitaDoctorView.as_view(), name='citas'),
    url(r'^agrega-consulta/(?P<pk>\w+)/', views.agregar_consulta, name='agregar_consulta'),
    url(r'^modificar-consulta/(?P<pk>\w+)/', views.modificar_consulta, name='modificar_consulta'),
    url(r'^eliminar-consulta/(?P<pk>\w+)/', views.eliminar_consulta, name='eliminar_consulta'),
    url(r'^ver-paciente/', views.VerPacientes.as_view(), name='ver_paciente'),
    url(r'^ultima-consulta/', views.UltimaConsulta.as_view(), name='ultima_consulta'),
    url(r'^ver-consulta/(?P<pk>\w+)/', views.VerConsultas.as_view(), name='ver_consulta'),
    url(r'^ver-examen/(?P<pk>\w+)/', views.ver_examen, name='ver_examen'),
    url(r'^agregar-examen/(?P<pk>\w+)/', views.agregar_examen, name='agregar_examen'),
    url(r'^modificar-examen/(?P<pk>\w+)/', views.modificar_examen, name='modificar_examen'),
    url(r'^guardar-examen/', views.GuardarExamen.as_view(), name='guardar_examen'),
    url(r'^historia-clinica/(?P<pk>\w+)/', views.historia_clinica, name='historia_clinica'),
    url(r'^agregar-antecedentes/', views.add_antecedentes, name='agregar_antecedentes'),
    url(r'^guardar-antecedentes/', views.save_antecentedes, name='guardar_antecedentes')
]

