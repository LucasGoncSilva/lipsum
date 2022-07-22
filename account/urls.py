from django.urls import path, URLPattern

from . import views


app_name = 'account'

urlpatterns: list[URLPattern] = [
    path('registrar', views.register_view, name='register'),
    path('entrar', views.login_view, name='login'),
    path('sair', views.logout_view, name='logout'),
]
