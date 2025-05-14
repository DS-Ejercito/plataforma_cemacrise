from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
import pandas as pd
from .models import *


list_deptos = depto.objects.all()
list_munic = munic.objects.all()
list_est_dano = est_dano.objects.all()


def inicio(request):

    return render(request, 'index.html')

def inicio_2(request):

    return render(request, 'core/base.html')

def dashboard(request):

    return render(request, 'cv/form_dashboard.html')

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
        cant = 1,
        img = request.FILES.get('imageInput') 
        ) 
    incidencia_reg.save()
    return frm_princ_incidencias(request, request.POST['id_incidencia'])

def load_municipios(request):
    depto_id = request.GET.get('depto_id')  # Obtener la ID de la marca desde la solicitud Ajax
    print(depto_id)
    municipios = munic.objects.filter(cod_depto=depto_id).order_by('descrip_corta')  # Filtrar modelos por marca
    return JsonResponse(list(municipios.values('id', 'descrip_corta')), safe=False)


def load_cv(request):
    
    cod_munic = request.GET.get('cod_munic')  # Obtener la ID de la marca desde la solicitud Ajax
    print(cod_munic)
    centros = cv.objects.filter(cod_munic=cod_munic).order_by('nom')  # Filtrar modelos por marca
    return JsonResponse(list(centros.values('id', 'nom')), safe=False)

def frm_princ_danos(request, tp_dano_p):
    tp_danos_v = get_object_or_404(tp_dano, id = tp_dano_p)
    dano = danos_ocasionados.objects.filter(tp_dano = tp_dano_p)
    context = {
        'tp_danos_info' : tp_danos_v,
        'danos' : dano
    }
    return render(request, 'danos/form_gen_danos.html', context)

def frm_reg_danos(request, tp_dano_p):
    tp_danos_v = get_object_or_404(tp_dano, id = tp_dano_p)
    context = {
        'tp_danos_info' : tp_danos_v,
        'departamentos' : list_deptos,
        'municipios' : list_munic,
        'est_dano' : list_est_dano
    }
    return render(request, 'danos/form_reg_danos.html', context)

def create_dano_bd(request):
    datetime_obj = datetime.strptime(request.POST['fch_hora'] , "%Y-%m-%dT%H:%M")
    fecha = datetime_obj.strftime("%Y-%m-%d")  # '2024-11-20'
    hora = datetime_obj.strftime("%H:%M")      # '12:36'
    dano_reg = danos_ocasionados(
        fecha = fecha ,
        hora = hora ,
        procedencia = procedencia.objects.get(id=1),
        tp_dano = tp_dano.objects.get(id=request.POST['id_dano']), 
        est_dano = est_dano.objects.get(id=request.POST['est_dano']),
        depto = depto.objects.get(id=request.POST['departamento']),
        munic = munic.objects.get(id=request.POST['municipio']),
        obser = request.POST['observ'],
        longitud = request.POST['longitude'],
        latitud = request.POST['latitude'],
        cant = 1,
        img = request.FILES.get('imageInput') 
        ) 
    dano_reg.save()
    return frm_princ_incidencias(request, request.POST['id_dano'])

def frm_princ_asist(request, tp_asist_p):
    tp_asis_v = get_object_or_404(tp_asist, id = tp_asist_p)
    asis = pers_asist.objects.filter(tp_asist = tp_asist_p)
    context = {
        'tp_asist_info' : tp_asis_v,
        'asist' : asis
    }
    return render(request, 'asistencias/form_gen_asist.html', context)

def frm_reg_asist(request, tp_asist_p):
    tp_asist_v = get_object_or_404(tp_asist, id = tp_asist_p)
    context = {
        'tp_asist_info' : tp_asist_v,
        'departamentos' : list_deptos,
        'municipios' : list_munic
    }
    return render(request, 'asistencias/form_reg_asist.html', context)

def create_asist_bd(request):
    datetime_obj = datetime.strptime(request.POST['fch_hora'] , "%Y-%m-%dT%H:%M")
    fecha = datetime_obj.strftime("%Y-%m-%d")  # '2024-11-20'
    hora = datetime_obj.strftime("%H:%M")      # '12:36'
    asist_reg = pers_asist(
        fecha = fecha ,
        hora = hora ,
        procedencia = procedencia.objects.get(id=1),
        tp_asist = tp_asist.objects.get(id=request.POST['id_asist']), 
        depto = depto.objects.get(id=request.POST['departamento']),
        munic = munic.objects.get(id=request.POST['municipio']),
        obser = request.POST['observ'],
        longitud = request.POST['longitude'],
        latitud = request.POST['latitude'],
        cant_anci = request.POST['cant_ancianos'],
        cant_mujeres = request.POST['cant_mujeres'],
        cant_hombres = request.POST['cant_hombres'],
        cant_ninos = request.POST['cant_ninos'],
        img = request.FILES.get('imageInput') 
        ) 
    asist_reg.save()
    return frm_princ_asist(request, request.POST['id_asist'])

def frm_princ_cv(request):
    cvs = cv.objects.all()
    context = {
        'cv' : cvs
    }
    return render(request, 'cv/form_gen_cv.html', context)
def frm_mapa(request):

    return render(request, 'cv/form_mapa.html')

def cargar_cv(request):
    if request.method == 'POST':
        cv.objects.all().delete()
        # Obtenemos el archivo subido
        archivo_excel = request.FILES['archivo_excel']
        
        # Leemos el archivo Excel con pandas
        try:
            df = pd.read_excel(archivo_excel)
            # Iteramos sobre las filas del DataFrame
            for index, row in df.iterrows():
                # Crear el contacto en la base de datos
                cv.objects.create(
                    cod_depto=depto.objects.get(id=row['Departamento']),
                    cod_munic=munic.objects.get(id=row['Municipio']),                    
                    latitud=row['Latitud'],
                    longitud=row['Longitud'],
                    nom=row['Nombre'],
                    procedencia=procedencia.objects.get(id=row['Unidad'])
                )
            return HttpResponse("Centro de Votacion Cargados Correctamente")
        except Exception as e:
            return HttpResponse(f"Error al cargar los centro de votacion: {e}")
    return render(request, 'cv/cargar_cv.html')

def cargar_guia(request):
    if request.method == 'POST':
        cv.objects.all().delete()
        archivo_excel = request.FILES['archivo_excel']
        try:
            df = pd.read_excel(archivo_excel)
            for index, row in df.iterrows():
                try:
                    cv.objects.create(
                        cod_depto=depto.objects.get(id=row['cod_depto']),
                        cod_munic=munic.objects.get(cod_munic=row['cod_munic']),
                        cod_area=area.objects.get(id=row['cod_area']),
                        latitud=row['latitud'],
                        longitud=row['longitud'],
                        sector_electoral=row['sector_electoral'],
                        carga_electoral=str(row['carga_electoral']),
                        nom=row['nom'],
                        cod_estado=estado.objects.get(id=row['cod_estado'])
                    )
                except Exception as fila_error:
                    print(f"Error en la fila {index + 2}: {fila_error}")
                    return HttpResponse(f"Error en la fila {index + 2}: {fila_error}")
            return HttpResponse("Centro de Votación cargados correctamente")
        except Exception as e:
            return HttpResponse(f"Error al procesar el archivo: {e}")
    
    return render(request, 'cv/cargar_guia_telefonica.html')

def guia_tel(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')  # Obtiene el parámetro de búsqueda
        contactos = Contacto.objects.all()
        return render(request, 'cv/form_guia_telefonica.html', {'contactos': contactos})
    
def registrar_manual(request):
    departamentos = depto.objects.all()
    return render(request, 'cv/form_registro.html', {'departamentos': departamentos})

def actualizar_cv(request):

    if request.method == 'POST':
        centro_id = request.POST.get('cv')  # ID del centro (cv.id)
        estado_id = request.POST.get('estado')  # ID del nuevo estado (clave foránea)
        nueva_img = request.FILES.get('imagen') # Imagen opcional
        print(centro_id )
        print(nueva_img)
        print(estado_id)
        try:
            centro = get_object_or_404(cv, id=centro_id)

            if estado_id:
                centro.cod_estado = get_object_or_404(estado, id=estado_id)

            if nueva_img:
                centro.img = nueva_img

            centro.save()
            return JsonResponse({'mensaje': 'Centro actualizado correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al actualizar: {e}'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)