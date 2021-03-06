"""
Django settings for django_ecommerce project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q0web^(o_e76l60)u9_v7cf#w_*&pfa=-0z1@tkwq$vo)5)2=('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['e-art-web.herokuapp.com']


STRIPE_PUB_KEY='pk_test_51JF0YyFu7LP4zPGhlseHc8ymifUe3UmQxI7SIOv9q2YtEoAH4xDwhxWDhDhVNkNbQhUncnVfBjgTYWrVtIEzRd4U00ni72nftz'
STRIPE_SECRET_KEY='sk_test_51JF0YyFu7LP4zPGh5HlkpuG0YXAgZBbfkC1bqWwOjncQbyuTaWhXMCB7VKb4rChUexhiDEewui2Z3AX0jk65g2fN00DxyVtO2j'
LOGIN_URL='login'

LOGIN_REDIRECT_URL='vendor_admin'

LOGOUT_REDIRECT_URL='frontpage'


#one day in seconds which saves the products in cart before the refresh
SESSION_COOKIE_AGE=86400    
CART_SESSION_ID='cart'




EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'eriseldashehaj@gmail.com'
EMAIL_HOST_PASSWORD = 'W0nd3rland2021!.123'
DEFAULT_EMAIL_FROM='Interior store <noreply@codewithstein.com>'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.order',
    'apps.cart',
    'apps.core',
    'apps.vendor',
    'apps.product',
    'widget_tweaks',
   
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

ROOT_URLCONF = 'django_ecommerce.urls'


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
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'ddi2cj00490kgv',
        'HOST': 'ec2-34-249-247-7.eu-west-1.compute.amazonaws.com',
        'USER': 'mvlkuqqbtatlus',
        'PORT':'5432',
        'PASSWORD':'902496153cea510e05ba82f641c9d5863e752f237614d13fcf964e606d1fe32a',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
#DEVELOPMENT
#STATIC_URL='/static/'

#STATICFILES_DIRS=[
 #    BASE_DIR / 'static']
 
 #PRODUCTION
 STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
 STATIC_URL="/static/"
 django_heroku.settings(locals())
 
 


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL='/media/'
MEDIA_ROOT= BASE_DIR / 'media/'


#Email settings

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT='587'
EMAIL_HOST_USER='info.doit@gmail.com'
EMAIL_HOST_PASSWORD='q1w2e3r4t5y6'
EMAIL_USE_TLS= True


