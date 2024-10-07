
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('', inicio,name='INICIO'),
    path('quienes_somos',quienes_somos,name='QS'),
    path('reserva',reserva,name='RE'),
    path('contacto',contacto,name='CO'),
    path('habitaciones',habitaciones,name='HA'),
    path('habitacion/<id>/',det_habitacion,name='DA'),
    path('servicios',servicios,name='SE'),  
    path('testimonios',testimonial,name='TE'),   
    path('acerca',acerca,name='AS'),   
    path('login',login,name='LO'),  
    path('cerrar',cerrar_sesion,name='CC'),   
    path('registro_turista',registro_turista,name='RETU'),    
    path('registro_habitacion',registro_habitacion,name='REHA'),   
    path('listado_habitaciones',listado_habitaciones,name='LH'), 
    path('agregar_galeria',insertar_galeria,name="IG"), 
    path('envio_qr',enviar_codigo_qr,name="EQR"),
    path('reservar',reservar,name="RESERVAR"),
    path('qr', generar_qr2, name='qr'),
    
]
