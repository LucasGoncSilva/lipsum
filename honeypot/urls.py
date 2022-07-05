from django.urls import path, re_path, URLPattern

from . import views


app_name = 'honeypot'

urlpatterns: list[URLPattern] = [
    path('', views.honeypot, name='empty_redirect'),
    path('<path:path>', views.honeypot, name='redirect'),
    re_path(r'^(?P<path>.*)/$', views.honeypot, name='re_redirect'),
    path('login', views.honeypot, name='honeypot')
]
