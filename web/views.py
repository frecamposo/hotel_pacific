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

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from django.core.mail import EmailMessage
# Create your views here.

def inicio(request):
    request.session["datos"]=""
    x={}

    # x["valor"]=request.session["datos"]
    # x["habitacion"]=habi(0)
    comentarios=Comentario.objects.all()
    mensaje={'comentarios':comentarios}
    return render(request,"index.html",mensaje)

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
    comentarios=Comentario.objects.all()
    contexto['comentarios']=comentarios
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

    
def listado_habitaciones(request):
    hab=Habitacion.objects.all()
    contexto={'lista_h':hab}
    return render(request,"listado_habitaciones.html",contexto)


def det_habitacion(request,id):
    habitacion = Habitacion.objects.get(id_h=id)
    comentarios = Comentario.objects.filter(id_h=habitacion)
    fotos=Galeria.objects.filter(id_h=habitacion)
    mensaje=""
    if request.POST:
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        id_h = request.POST.get("id_h")
        comentario = request.POST.get("comentario")
        fecha_actual = datetime.now()
        fecha_solo = fecha_actual.date()
        mensaje=""
        print("entro")
        try:
            come=Comentario()
            come.comentario=comentario
            come.correo=email
            come.fecha_creacion=fecha_solo
            come.nombre=nombre
            come.id_h=habitacion
            come.save()
            mensaje="Comentario Registrado"
            print("Grabado")
        except BaseException as error:
            mensaje=error
            print("mensaje")
    cantidad_comentarios=Comentario.objects.filter(id_h=habitacion).count()
    contexto={'habitacion':habitacion,'comentarios':comentarios,"cantidad":cantidad_comentarios}
    contexto["mensaje"]=mensaje
    contexto["fotos"]=fotos
    return render(request,"habitacion.html",contexto)

def insertar_galeria(request):
    mensaje=""
    if request.POST:
        habitacion = request.POST.get("habitacion")
        imagen = request.FILES.get("imagen")
        obj_hab = Habitacion.objects.get(id_h=habitacion)

        gale = Galeria()
        gale.descripcion=''
        gale.foto=imagen
        gale.id_h=obj_hab
        gale.save()
        mensaje = "Agrego Imagen para habitacion "

    hab=Habitacion.objects.all()
    contexto={'lista_h':hab,"mensaje":mensaje}
    return render(request,"listado_habitaciones.html",contexto)

     
def login(request):
    contexto = {}
    if request.POST:
        nombre = request.POST.get("email")
        password = request.POST.get("pass")
        us = authenticate(request,username=nombre,password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request,"index.html",contexto)
        else:
            contexto = {"mensaje":"usuario y contraseña incorrecto"}
            return render(request,"login.html",contexto)        
    return render(request,"login.html",contexto)


def enviar_codigo_qr(request):
    # Datos que quieres convertir en un código QR
    data = "https://www.ejemplo.com"  # Reemplázalo con la URL o información que desees

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crear la imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen en un buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Crear el mensaje de correo electrónico
    email = EmailMessage(
        subject='fre.campos@duocuc.cl',
        body='Adjunto encontrarás tu código QR.',
        from_email='campos.fm@gmail.com',  # Reemplaza con tu correo
        to=['fre.campos@duocuc.cl'],   # Reemplaza con el correo del destinatario
    )

    # Adjuntar la imagen del código QR
    email.attach('codigo_qr.png', buffer.getvalue(), 'image/png')

    # Enviar el correo
    email.send()

    comentarios=Comentario.objects.all()
    contexto={'comentarios':comentarios}
    contexto["mensaje"]="OK"
    return render(request,"index.html",contexto)


def reserva(request,id):
    habitacion = Habitacion.objects.get(id_h=id)
    comentarios = Comentario.objects.filter(id_h=habitacion)
    fotos=Galeria.objects.filter(id_h=habitacion)
    mensaje=""
    if request.POST:
        f_inicio = request.POST.get("date3")
        f_termino= request.POST.get("date4")
        id_h = request.POST.get("id_h")
        comentario = request.POST.get("comentario")
        fecha_actual = datetime.now()
        fecha_solo = fecha_actual.date()
        mensaje=""
        print("entro")
        try:
            come=Comentario()
            come.comentario=comentario
            come.correo=email
            come.fecha_creacion=fecha_solo
            come.nombre=nombre
            come.id_h=habitacion
            come.save()
            mensaje="Comentario Registrado"
            print("Grabado")
        except BaseException as error:
            mensaje=error
            print("mensaje")
    cantidad_comentarios=Comentario.objects.filter(id_h=habitacion).count()
    contexto={'habitacion':habitacion,'comentarios':comentarios,"cantidad":cantidad_comentarios}
    contexto["mensaje"]=mensaje
    contexto["fotos"]=fotos
    return render(request,"habitacion.html",contexto)


def cerrar_sesion(request):
    contex = {}
    logout(request)
    return render(request,"index.html",contex)
    
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

def registro_habitacion(request):
    contex={}
    if request.POST:
        # Si solo quieres la fecha actual
        try:
            piso= request.POST.get("piso")
            numero = request.POST.get("numero")
            cant_personas = request.POST.get("cant_personas")
            cant_hab = request.POST.get("cant_hab")
            cant_banos=request.POST.get("cant_banos")
            metros=request.POST.get("metros")
            wifi=request.POST.get("wifi")
            tv=request.POST.get("tv")
            desayuno=request.POST.get("desayuno")
            precio=request.POST.get("precio")
            estrellas=request.POST.get("estrellas")
            descripcion=request.POST.get("descripcion")
            tipo_habitacion=request.POST.get("tipo_habitacion")
            ima  = request.FILES.get("imagen")
            ha=Habitacion()
            ha.activa='s'
            ha.banos=cant_banos
            ha.cant_personas=cant_personas
            ha.desayuno=desayuno
            ha.descripcion=descripcion
            ha.habitaciones=cant_hab
            ha.id_th=TipoHabitacion.objects.get(id_th=tipo_habitacion)
            ha.imagen=ima
            ha.metros=metros
            ha.num_star=estrellas
            ha.numero=numero
            ha.piso=piso
            ha.precio_noche=precio
            ha.tv_cable=tv
            ha.wifi=wifi
            ha.save()
            contex["mensaje"]="Grabo"        
        except BaseException as error:                                       
            contex = {"nada":''}
            return render(request, "index.html",contex) 
      
    tipo_h=TipoHabitacion.objects.all()
    contex["t_hab"]=tipo_h     
    return render(request,"registro_habitacion.html",contex)
