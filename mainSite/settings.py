"""
Django settings for mainSite project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from os import environ, mkdir
from os.path import abspath, basename, dirname, isdir, join, normpath
from sys import path
import mainSite
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = dirname(mainSite.__file__)
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v520djd)h1ckxg*_48$(k!lt_pyc=_i@*7*vl58(qm1h8tp=zv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.58.129', '0.0.0.0', 'localhost', '*']


# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'home.apps.HomeConfig',
    'onboarding.apps.OnboardingConfig',
    'django.contrib.admin',         #(dev, madrid2017)
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mainSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'mainSite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CIMD',
        'USER': 'camsuser',
        'PASSWORD': 'camspass',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    join(SITE_ROOT, "static/"),
    '/static/',
    ]

#MEDIA_ROOT = join(BASE_DIR, 'media')
# ======== MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = join(DJANGO_ROOT, 'media/')
if not isdir(MEDIA_ROOT):
    raise Exception('MEDIA_ROOT is not a valid path!!! Please check mainSite/settings.py')
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# ======== END MEDIA CONFIGURATION