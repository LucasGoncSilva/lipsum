from django.contrib import admin
from django.urls import path, include, URLPattern
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns: list[URLPattern] = [
    # Adm pages
    path('__manager__/', admin.site.urls),
    path('admin/', include('honeypot.urls')),
    # System functionality's pages
    path('conta/', include('account.urls')),
    path('reset', PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('reset-enviado', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-concluido', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('captcha/', include('captcha.urls')),
    # User's pages
    path('', include('home.urls')),
    path('segredos/', include('secret.urls')),
]


handler403 = 'err.views.handle403'
handler404 = 'err.views.handle404'
handler500 = 'err.views.handle500'
