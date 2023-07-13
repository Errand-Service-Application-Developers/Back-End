from .common import * 


SECRET_KEY = 'django-insecure-n6y_j(97k_9@8ny7#@f!eoxn63q3y5t4px715b2z1e=_l_npk*'


ALLOWED_HOSTS = ['192.168.43.173']

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'errandgo',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'macquena'
    }
}
