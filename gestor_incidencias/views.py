from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *

def inicio(request):
    return render(request, 'index.html')

def inicio_2(request):
    return render(request, 'base.html')
