"""
Django settings for ShipEast project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*h6%4z_ye=i794f50!t#)9rltqszw=_y(0u)!s4afg6+-y5p)7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['realmad.pythonanywhere.com','127.0.0.1', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'account',
    'inventory',
    'sitemap',
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

ROOT_URLCONF = 'ShipEast.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ShipEast.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',#'django.db.backends.sqlite3',#'django.db.backends.mysql',#
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # 'realmad', ship_east',#os.path.join(BASE_DIR, 'db.sqlite3'), #
        #'USER': 'root',
        #'PASSWORD': '', #'micantboda123',
        #'HOST': 'realmad.mysql.pythonanywhere-services.com',
    }
#    'server': {
#
#    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#################################################
# Developers Additional Configuration 
#################################################

# Static Files
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'public'),
    os.path.join(BASE_DIR, 'static'),
)

## Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.normpath(BASE_DIR), "public", "media")


## Email Configuration
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'support@shipeastcouriers.com'
EMAIL_HOST_PASSWORD = 'micantboda123+'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'Admin <{}>'.format(EMAIL_HOST_USER)
SERVER_EMAIL = 'support@shipeastcouriers.com'

# Session and Security
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 12096 #1209600
SESSION_SAVE_EVERY_REQUEST = True
SECURE_BROWSER_XSS_FILTER = True
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Authentication
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

from django.contrib import messages

# Message
MESSAGE_TAGS = {
	messages.DEBUG: 'primary',
	messages.INFO: 'info',
	messages.SUCCESS: 'success',
	messages.WARNING: 'warning',
	messages.ERROR: 'danger',
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'