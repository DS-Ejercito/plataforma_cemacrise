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
    path('create_inc_bd/', views.create_inc_bd, name='create_inc_bd'),
    ]
