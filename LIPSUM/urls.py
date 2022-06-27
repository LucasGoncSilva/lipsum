from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Adm pages
    path('__manager__/', admin.site.urls),
    path('admin/', include('honeypot.urls')),
    # System functionality's pages
    path('conta/', include('accounts.urls')),
    path('captcha/', include('captcha.urls')),
    # User's pages
    path('', include('home.urls')),
    path('segredos/', include('secret.urls')),
]

# TODO: handle common errors
# handler403 = 'hub.views.error403'
# handler404 = 'hub.views.error404'
# handler500 = 'hub.views.error500'

# TODO: set password recovery
