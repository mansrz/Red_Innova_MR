# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import http
from django.contrib import auth


def home(request):
    return render(request, 'index.html')

def static_page(request, page):
    return render(request, page)

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
            return http.HttpResponseRedirect('/')
        else:
            context = {'error': 'User or password is wrong'}
    else:
        context = {}

    return render(request, 'sign-in.html', context)


# Create your views here.
#login
#formularios de registro
#profile
# 
