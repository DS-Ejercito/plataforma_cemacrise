from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio_2/', views.inicio_2, name='inicio_2'),
    ]