import environ

from PASS_MANAGER.settings.base import *


env = environ.Env()


DATABASES = {
    'default': env.db()
}
