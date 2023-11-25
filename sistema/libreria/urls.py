from django.urls import path 
from . import views
from .views import planes_y_precios

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('planes_y_precios/', planes_y_precios, name='planes_y_precios'),
    path('acerca_de_nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('registro/', views.registro, name='registro'),
    path('registro/emprendedor/', views.registrar_emprendedor, name='registrar_emprendedor'),
    path('explorar/', views.explorar, name='explorar'),
    path('explorar/registrar_emprendimiento/', views.registrar_emprendimiento, name='registrar_emprendimiento'),
    path('registro/empresa_grande/', views.registrar_empresa_grande, name='registrar_empresa_grande')]