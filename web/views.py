from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def static_page(request, page):
    return render(request, page)
