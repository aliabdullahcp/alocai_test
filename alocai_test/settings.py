"""
Django settings for alocai_test project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
import environ
root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('ALOCAI_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('ALOCAI_DEBUG', default=True)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'games',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
  'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

ROOT_URLCONF = 'alocai_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alocai_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str('ALOCAI_DEFAULT_DATABASE_NAME', 'alocai'),
        "USER": env.str('ALOCAI_DEFAULT_DATABASE_USER', "postgres"),
        "PASSWORD": env.str('ALOCAI_DEFAULT_DATABASE_PASSWORD', "Shah123"),
        "HOST": env.str('ALOCAI_DEFAULT_DATABASE_HOST', "localhost"),
        "PORT": env.str('ALOCAI_DEFAULT_DATABASE_PORT', "5432")
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'ALOCAI API',
    'DESCRIPTION': """These are the APIs that can be consumed using HTTP/HTTPS requests.

    Common Error Responses:-
      - 400 : Bad request
      - 401 : Un-authorized access
      - 404 : Record not found
      - 503 : Service unavailable

    Example Error Responses:-
      Example 1:
        {
            "ser-attribute"   : [ "Error 1", "Error 2" ], 
            "ser-attribute2"  : [ "Error 1" ]
        }
  """,
    'VERSION': '1.0.0',
    'COMPONENT_SPLIT_REQUEST': True,
}

SPECTACULAR_DEFAULTS = {
    'POSTPROCESSING_HOOKS': [
        'docs.views.test'
    ],
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = env.str('ALOCAI_LANGUAGE_CODE', default='en-us')

TIME_ZONE = env.str('ALOCAI_TIME_ZONE', default='UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = env.bool('ALOCAI_USE_TZ', default=True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = env.str('ALOCAI_STATIC_URL')
STATIC_ROOT = os.path.join(str(root), env.str('ALOCAI_STATIC_ROOT'))

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = env.str('ALOCAI_MEDIA_URL')
MEDIA_ROOT = os.path.join(BASE_DIR, env.str('ALOCAI_MEDIA_ROOT'))
