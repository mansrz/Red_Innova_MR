#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'index.html')

def static_page(request, page):
    return render(request, page)

def login(request):
    if request.method == 'POST':
        try:
            username = request.GET['username']
            password = request.GET['password']
        except:
            return HttpResponse('Malos Parametros ')
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user)
            entidad = user.entidad_set.all()
            
            response_content = {
                'username': user.username,
            }
        else:
            return HttpResponseBadRequest('Usario o contraseña incorrecto')
            
def profile(request):
    try:
        user = request.user
    except:
        HttpResponseBadRequest('Necesita hacer login')

    if user.is_authenticated():
        context = {
            'user' : user
        }
        return render(raequest, 'profile.html',context)
    else:
        return HttpResponseForbidden()
            
def search(request):
    term = request.GET.get('term')
    if not term:
        return redirect('/')

    #Para buscar personas tanto naturales como instituciones
    resultado = Persona.objects.filter(name__contains = term.lower())
    if len(resultado) > 0:
      result = 'No hay incidencias'

    context ={
      'resultado' : resultado
    }
    return 
    response = render_to_response('web/search.json',context,context_instance= RequestContext(request))

    response['Content-Type'] = 'application/json; charset=utf-8'
    return response
  


# Create your views here.
#login
#formularios de registro
#profile
# 
