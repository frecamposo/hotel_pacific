from django.shortcuts import render
from .i18n import *

from .models import *
# importar el modelo de tabla User 
from django.contrib.auth.models import User,Group
# importar librerias que permitan la validacion del login
from django.contrib.auth import authenticate,logout,login as login_aut
# importar libreria decoradora que permite evitar el ingreso de usuarios a las paginas web
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import redirect
from datetime import datetime

# Create your views here.
def crear_usuario(request):
    if request.POST:
        # Si solo quieres la fecha actual
        identificacion= request.POST.get("identificacion")
        nombre = request.POST.get("nombre")
        ape_paterno = request.POST.get("ap_paterno")
        ape_materno = request.POST.get("ap_materno")
        es_nacional=request.POST.get("es_nacional")
        pais=request.POST.get("pais")
        habla_espanol=request.POST.get("habla_espanol")
        idioma_natural=request.POST.get("idioma")

        fecha_solo = fecha_actual.date()

        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        fecha_creacion = fecha_solo
        activo=1
        if pass1!=pass2:
            contexto= {"mensaje":"contraseñas son diferentes"}
            return render(request,"crear_usuario.html",contexto)

        try:
            usu = User.objects.get(username=nom_usuario)
            contexto = {"mensaje":"nombre de usuario existe"}
            return render(request,"crear_usuario.html",contexto)
        except:  
            grupo=Group.objects.get(name='colaboradores')


            usu = User()
            usu.first_name=nombre
            usu.last_name=apellido
            usu.email=email
            usu.username=nom_usuario
            usu.set_password(pass1)
            usu.save()
            usu.groups.add(grupo)
            us = authenticate(request,username=nom_usuario,password=pass1)
            login_aut(request,us)

            categorias = Categoria.objects.all()
            contex = {"categorias":categorias}
            return render(request, "index.html",contex)        
    return render(request,"crear_usuario.html")




def inicio(request):
    request.session["datos"]=""
    x={}

    # x["valor"]=request.session["datos"]
    # x["habitacion"]=habi(0)
    return render(request,"index.html",x)

def quienes_somos(request):
    contexto={}
    return render(request,"quienes_somos.html",contexto)

def reserva(request):
    contexto={}
    return render(request,"booking.html",contexto)

def contacto(request):
    contexto={}
    return render(request,"contact.html",contexto)

def habitaciones(request):
    lista_habitaciones=Habitacion.objects.all()
    contexto={'lista':lista_habitaciones}
    contexto['loop_times'] = range(1, 2)
    return render(request,"room.html",contexto)

def servicios(request):
    contexto={}
    return render(request,"service.html",contexto)

def testimonial(request):
    contexto={}
    return render(request,"testimonial.html",contexto)
    
def acerca(request):
    contexto={}
    return render(request,"acerca.html",contexto)

def det_habitacion(request):
    contexto={}
    return render(request,"habitacion.html",contexto)
        

def login(request):
    contexto={}
    return render(request,"login.html",contexto)
    
def registro_turista(request):
    if request.POST:
        # Si solo quieres la fecha actual
        identificacion= request.POST.get("identificacion")
        nombre = request.POST.get("nombre")
        ape_paterno = request.POST.get("ap_paterno")
        ape_materno = request.POST.get("ap_materno")
        es_nacional=request.POST.get("es_nacional")
        pais=request.POST.get("pais")
        habla_espanol=request.POST.get("habla_espanol")
        idioma_natural=request.POST.get("idioma")
       
        fecha_actual = datetime.now()
        fecha_solo = fecha_actual.date()

        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        fecha_creacion = fecha_solo
        activo=1
        if pass1!=pass2:
            contexto= {"mensaje":"contraseñas son diferentes"}
            return render(request,"registro.html",contexto)

        try:
            usu = User.objects.get(username=email)
            contexto = {"mensaje":"nombre de usuario existe"}
            return render(request,"registro.html",contexto)
        except:  
            grupo=Group.objects.get(name='colaboradores')
            usu = User()
            usu.first_name=nombre
            usu.last_name=ape_paterno
            usu.email=email
            usu.username=email
            usu.set_password(pass1)
            usu.save()
            usu.groups.add(grupo)
            print(usu)
            us = authenticate(request,username=email,password=pass1)
            login_aut(request,us)

            try:
                usuarios=Usuarios()
                usuarios.activo='S'
                usuarios.correo=email
                usuarios.fecha_creacion=fecha_solo
                usuarios.password=pass1
                usuarios.save()
                cli=Cliente()
                cli.identificacion=identificacion
                cli.nombre=nombre
                cli.ape_paterno=ape_materno
                cli.ape_materno=ape_materno
                cli.es_nacional=es_nacional
                cli.pais=pais
                cli.habla_espanol=habla_espanol
                cli.idioma_natural=idioma_natural
                cli.id_user=usuarios
                cli.save()
            except BaseException as errror:
                print('errror:',errror)
            contex = {"nada":''}
            return render(request, "index.html",contex) 
    contex={}       
    return render(request,"registro.html",contex)
