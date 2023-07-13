import os
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = ['errandgo-prod-29e25f29f785.herokuapp.com']



DATABASES = {
     'default': dj_database_url.config()
      
}
