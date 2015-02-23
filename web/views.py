#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django import http
from django.contrib import auth
from django.template import RequestContext
from forms import * 


def home(request):
    return render(request, 'index.html')

def static_page(request, page):
    return render(request, page)

def signup(request):
    form_institucion = InstitucionForm()
    form_persona = PersonaForm()
    form_user = UserForm()  

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_type = request.POST['type']

        if user_form.is_valid():
            user = User(
                      username= user_form.cleaned_data['username'],
                      password = user_form.cleaned_data['password'],
                    )
            # Add valid user to parameters
            request.POST.update(user=user.pk)

            if user_type == 'INSTITUCION':
                EntidadForm = InstitucionForm
            elif user_type == 'PERSONA':
                EntidadForm = PersonaForm
            else:
                raise Exception('Invalid type')
                return HttpResponseBadRequest('Invalid type')

            entidad_form = EntidadForm(request.POST)

            if entidad_form.is_valid():
                user.save()
                entidad_form.save()

                from django.http import HttpResponse
                return HttpReponse('ok')

    return render_to_response('sign-up.html',
                              {'form_institucion': form_institucion,
                               'form_persona': form_persona,
                               'form_user': form_user, },
                              context_instance=RequestContext(request))

def signup_institucion(request):
    if request.method == "POST":
        tipo = request.GET.get('tipo')
        print tipo
    else:
        formset = InstitucionForm()
    return render_to_response("sign-up.html", {"formset": formset,})
        

def signup_persona(request):
    pass

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            # Bad parameters
            return http.HttpResponseRedirect('/')
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            # TODO redirect to profile
            return http.HttpResponseRedirect('/home.html')
        else:
            context = {'error': 'User or password is wrong'}
    else:
        context = {}
    return render(request, 'sign-in.html', context)

def logout(request):
    auth.logout(request)
    return http.HttpResponseRedirect('/')
          
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
  

