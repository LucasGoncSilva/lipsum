from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'home'

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
]
