from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Auto

from inicio.forms import CrearAuto

import random

def inicio(request):
   # return HttpResponse('Bienvenidos a mi INICIO!!')
   return render(request, 'inicio/index.html')

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    return HttpResponse(f'<h1> Mi template1 <h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido} {edad}')

def template2(request, nombre, apellido, edad):
   
    archivo_abierto = open(r'C:\Users\tobia\Escritorio\CoderHouse\MiProyecto\templates\template2.html')
    # archivo_abierto = open('templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha = datetime.now()
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
    }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def template3(request, nombre, apellido, edad):
   
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
    }
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

def template4(request, nombre, apellido, edad):
    
    fecha = datetime.now()
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
    }
    
    return render(request, 'template2.html', datos)

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})

def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo=modelo )
    auto.save()
    return render(request, 'auto_templates/creacion.html', {'auto': auto})

def crear_auto_v2(request):
    
    # v1
    # print('Valor de la request: ', request)
    # print('Valor de la GET: ', request.GET)
    # print('Valor de la POST: ', request.POST)
    
    # if request.method == 'POST':
    #     auto = Auto(marca=request.POST.get('Marca'), modelo=request.POST.get('Modelo'))
    #     auto.save()
    
    # return render(request, 'inicio/crear_auto_v2.html')
    
    # v2
    print('Valor de la request: ', request)
    print('Valor de la GET: ', request.GET)
    print('Valor de la POST: ', request.POST)
    
    formulario = CrearAuto()
    
    if request.method == 'POST':
        formulario = CrearAuto(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            auto = Auto(marca=datos.get('marca'), modelo=datos.get('modelo'))
            auto.save()
            return redirect('autos')
            
    return render(request, 'inicio/crear_auto_v2.html', {'formulario': formulario})

def autos(request):
    
    autos = Auto.objects.all()
    
    return render(request, 'inicio/autos.html', {'autos': autos})