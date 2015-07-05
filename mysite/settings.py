#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tsbn-gqj-e_)pq4q1ruy-o=!@!74skijqdv(@tciv)jh(q^)si'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME':'myDatabaseName',
        # 'USER':'root',
        # 'PASSWORD':'passwd',
        # 'HOST':'127.0.0.1',
        # 'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN.utf-8'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATIC_JS = os.path.join(BASE_DIR,'static/js/').replace('\\','/')
STATIC_CSS = os.path.join(BASE_DIR,'static/css/').replace('\\','/')
STATIC_IMG = os.path.join(BASE_DIR,'static/images/').replace('\\','/')
STATIC_FONTS = os.path.join(BASE_DIR,'static/images/').replace('\\','/')

STATICFILES_DIRS = (
    ('js',os.path.join(STATIC_ROOT,'js') ),
    ('css',os.path.join(STATIC_ROOT,'css') ),
    # ('img',os.path.join(STATIC_ROOT,'img') ),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    # os.path.join(BASE_DIR,'apps/blog/templates')
)

# logging configuration
LOGGING = {
      'version': 1,
      'disable_existing_loggers': True,
      'formatters': {
          'simple': {
              'format': '[%(asctime)s] %(levelname)s : %(message)s'
          },
          'verbose': {
              'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d : %(message)s'
         },
     },
     'handlers': {
         'null': {
             'level': 'DEBUG',
             'class': 'django.utils.log.NullHandler',
         },
         'console': {
             'level': 'DEBUG',
             'class': 'logging.StreamHandler',
             'formatter': 'simple',
         },
         'file': {
             'level': 'DEBUG',
             'class': 'logging.FileHandler',
             'formatter': 'simple',
             'filename': os.path.join(BASE_DIR, 'logs/all.log'),
             'mode': 'a',
         },
     },
     'loggers': {
         'django.request': {
              'handlers': ['file', 'console'],
             'level':'DEBUG',
             'propagate': True,
         },
     },
}