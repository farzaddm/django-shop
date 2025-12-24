from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure--3x1nmolp5^e8x!*g8#)^1!t1lbt63s2*6l*0-x3u&bxs+-_oc'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': 'mysql',
        'PORT': config("DB_PORT", default="3306"),
    }
}

DEBUG_TOOLBAR_CONFIG = {
  'SHOW_TOOLBAR_CALLBACK': lambda request: True
}

