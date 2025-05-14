from django.urls import path

from plataforma_cemacrise import settings
from . import views
from django.conf.urls.static import static
from plataforma_cemacrise.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio_2/', views.inicio_2, name='inicio_2'),
    path('incidencias/<int:tp_incidencia_p>', views.frm_princ_incidencias, name='incidencias'),
    path('incidencias_registro/<int:tp_incidencia_p>', views.frm_reg_incidencias, name='incidencias_registro'),
    path('load-municipios/', views.load_municipios, name='load_municipios'),
    path('load-cv/', views.load_cv, name='load_cv'),
    path('create_inc_bd/', views.create_inc_bd, name='create_inc_bd'),
    path('danos/<int:tp_dano_p>', views.frm_princ_danos , name='danos'),
    path('danos_registro/<int:tp_dano_p>', views.frm_reg_danos, name='danos_registro'),
    path('create_dano_bd/', views.create_dano_bd, name='create_dano_bd'),
    path('asistencias/<int:tp_asist_p>', views.frm_princ_asist , name='asistencias'),
    path('asistencias_registro/<int:tp_asist_p>', views.frm_reg_asist ,name='asistencias_registro'),
    path('create_asistencias_bd/', views.create_asist_bd, name='create_asistencias_bd'),
    path('cargar_cv/', views.cargar_cv, name='cargar_cv'),
    path('cargar_guia_tel/', views.cargar_guia, name='cargar_guia'),
    path('cv', views.frm_princ_cv , name='cv'),
    path('mapa', views.frm_mapa , name='mapa'),
    path('guia', views.guia_tel , name='guia_tel'),
    path('dashboard', views.dashboard , name='dashboard'),
    path('registrar/', views.registrar_manual, name='registrar_manual'),
    path('actualizar_cv/', views.actualizar_cv, name='actualizar_cv'),

    ]
