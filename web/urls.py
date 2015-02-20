from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^sign-in.html$', views.login),
    url(r'^sign-out.html$', views.logout),
    url(r'^(.*\.html)$', views.static_page),
    url(r'^profile$', views.profile),
)
