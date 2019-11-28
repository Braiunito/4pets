from .base import *

DATABASES = {
    'default': {        
        'ENGINE': 'django.db.backends.postgresql',       
        'NAME': 'forpets',
        'USER': '4pets',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '',
        'DEFAULT_CHARSET': 'utf-8',
    }
}
