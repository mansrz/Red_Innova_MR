from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^(.*\.html)$', views.static_page),
)
