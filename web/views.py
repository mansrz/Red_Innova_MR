from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth import authenticate, login













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
            response_content = {
                'username': user.username,

            }
        else:
            return HttpResponseBadRequest('Usario o contraseña incorrecto')
            


# Create your views here.
#login
#formularios de registro
#profile
# 
