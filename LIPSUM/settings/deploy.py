import environ

from LIPSUM.settings.base import *


env = environ.Env()


DATABASES = {
    'default': env.db()
}
