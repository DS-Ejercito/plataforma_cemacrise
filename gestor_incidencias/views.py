from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *

list_deptos = depto.objects.all()
list_munic = munic.objects.all()

def inicio(request):
    return render(request, 'index.html')

def inicio_2(request):
    return render(request, 'core/base.html')

def frm_princ_incidencias(request, tp_incidencia_p):
    tp_incidenvia_v = get_object_or_404(tp_incidencia, id = tp_incidencia_p)
    incidencias = incidencia.objects.filter(tp_incidencia = tp_incidencia_p)
    context = {
        'tp_incidencia_info' : tp_incidenvia_v,
        'incidencia_filtrada' : incidencias
    }
    return render(request, 'incidencias/form_gen.html', context)

def frm_reg_incidencias(request, tp_incidencia_p):
    tp_incidenvia_v = get_object_or_404(tp_incidencia, id = tp_incidencia_p)
    context = {
        'tp_incidencia_info' : tp_incidenvia_v,
        'departamentos' : list_deptos,
        'municipios' : list_munic
    }
    return render(request, 'incidencias/form_reg_ins.html', context)

def create_inc_bd(request):
    datetime_obj = datetime.strptime(request.POST['fch_hora'] , "%Y-%m-%dT%H:%M")
    fecha = datetime_obj.strftime("%Y-%m-%d")  # '2024-11-20'
    hora = datetime_obj.strftime("%H:%M")      # '12:36'
    if request.POST['txt_cant'] :
        request.POST['txt_cant'] = 1
    incidencia_reg = incidencia(
        fecha = fecha ,
        hora = hora ,
        procedencia = procedencia.objects.get(id=1),
        tp_incidencia = tp_incidencia.objects.get(id=request.POST['id_incidencia']), 
        depto = depto.objects.get(id=request.POST['departamento']),
        munic = munic.objects.get(id=request.POST['municipio']),
        obser = request.POST['observ'],
        longitud = request.POST['longitude'],
        latitud = request.POST['latitude'],
        cant = request.POST['txt_cant'],
        img = request.FILES.get('imageInput') 
        ) 
    incidencia_reg.save()
    return frm_princ_incidencias(request, request.POST['id_incidencia'])

def load_municipios(request):
    depto_id = request.GET.get('depto_id')  # Obtener la ID de la marca desde la solicitud Ajax
    print(depto_id)
    municipios = munic.objects.filter(cod_depto=depto_id).order_by('descrip_corta')  # Filtrar modelos por marca
    return JsonResponse(list(municipios.values('id', 'descrip_corta')), safe=False)