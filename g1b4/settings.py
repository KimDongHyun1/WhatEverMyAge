"""
Django settings for g1b4 project.
Generated by 'django-admin startproject' using Django 2.2.3.
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
#SECRET_KEY = '-eb+6#hd7y5-p!j-mbc)y=ss+ss8-b598+#m3m-y0t&9s8m=n3'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '-eb+6#hd7y5-p!j-mbc)y=ss+ss8-b598+#m3m-y0t&9s8m=n3')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'api',
    'blog',
    'question',
    'users',

    'django.contrib.sites',       
    'rest_framework.authtoken',    
    'rest_auth',    
    'rest_auth.registration',    
    'allauth',    
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    #aws 배포
    #'storages',
]

# AWS_ACCESS_KEY_ID = 'AKIAY2J37TBFIZXL2AU5'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'sibtc-static'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'mysite/static'),
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'g1b4.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'g1b4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #postgresql
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'NAME': 'liondb',
        #'USER': 'postgres',
        #'PASSWORD': 'ehdgusdldi1!',
        #'HOST' : '127.0.0.1',
        #'PORT' : '5432', 
    }
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

#image 추가하기 위해 만든 것
MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

#회원가입 , 로그인
AUTH_USER_MODEL = 'users.CustomerUser' 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
SITE_ID =1 
ACCOUNT_LOGOUT_ON_GET = True

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# REST_FRAMEWORK = {
#     'DEFAULT_PARSER_CLASSES': (
#         'rest_framework.parsers.JSONParser',
#         'rest_framework.parsers.MultiPartParser',
#         #...
#     )
# }





REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.MyCustomTokenSerializer',

}
