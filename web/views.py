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
            


# Create your views here.
#login
#formularios de registro
#profile
# 
