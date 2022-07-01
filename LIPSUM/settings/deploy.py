import environ

from LIPSUM.settings.base import *


env = environ.Env()


DATABASES = {
    'default': env.db()
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
