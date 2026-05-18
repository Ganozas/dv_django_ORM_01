import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('DB_HOST')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')
name = os.getenv('DB_NAME')
user = os.getenv('DB_USER')

SECRET_KEY = os.getenv('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']


TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
