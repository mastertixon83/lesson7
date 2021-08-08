import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-wmvu07j_i@9fpyj2pq@#$j6(b9=u$u@apanaor8*wg9dsu^6$r'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myshop_db',
        'USER': 'tixon',
        'PASSWORD': 'gft654gfhgf',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
