
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio,name='INICIO'),
    path('quienes_somos',quienes_somos,name='QS'),
    path('reserva',reserva,name='RE'),
    path('contacto',contacto,name='CO'),
    path('habitaciones',habitaciones,name='HA'),
    path('habitacion',det_habitacion,name='DA'),
    path('servicios',servicios,name='SE'),  
    path('testimonios',testimonial,name='TE'),   
    path('acerca',acerca,name='AS'),   
    path('login',login,name='LO'),     
    path('registro_turista',registro_turista,name='RETU'),    
      
]
