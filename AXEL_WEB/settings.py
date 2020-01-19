import os
import sys
import random
import string

from django.conf.global_settings import ADMINS
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False

# Clé secrète selon l'environnement
if DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'c@n%u@91tum=@j392g20b8znh7dqfo-v%81))gxbbmu$=dy_*)')
else:
    SECRET_KEY = os.environ.get('SECRET_KEY', ')k7-35hzr=44j&_nls3u%*ne1xz@==1gt(1k9-6%ra!y6pk21l')


# Hôtes autorisés selon l'environnement
if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = ['axel-ihm.herokuapp.com']

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Applications installés
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'channels',
    'AdminAXEL.apps.AdminaxelConfig',
    'WebAXEL.apps.WebaxelConfig',
    'api.apps.ApiConfig',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
]

AUTH_USER_MODEL = 'WebAXEL.AxelUser'
AUTH_GROUP_MODEL = 'WebAXEL.AxelGroup'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ADMIN = ('Samy', 'xhackax47@gmail.com')
MANAGERS = ADMINS
ROOT_URLCONF = 'AXEL_WEB.urls'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.template.context_processors.i18n",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AXEL_WEB.wsgi.application'

# Bases de données
if not DEBUG and 'test' not in sys.argv or 'test_coverage' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'daskqm0c329l07',
            'USER': 'zxavxwjozlvyhd',
            'PASSWORD': '25e6d508fe5fd1fe7d823381ba8fb82077a629a74d811483274fd51e5dd14216',
            'HOST': 'ec2-54-247-72-30.eu-west-1.compute.amazonaws.com',
            'PORT': '5432',
        }
    }
elif DEBUG and 'test' not in sys.argv or 'test_coverage' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'AXEL_WEB',
            'USER': 'xhackax47',
            'PASSWORD': 'L@n@s@y@n34000',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Configuration BDD SQLITE pour CircleCI
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'AXEL_WEB',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalisation

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'static/locale/'),
)
gettext = lambda x: x

LANGUAGES = (
    ('fr', gettext('French')),
    ('en', gettext('English')),
)

# Channels
# ASGI_APPLICATION = "AXEL_WEB.routing.application"
# CHANNEL_LAYERS = {
#         'default': {
#                 'BACKEND': 'asgiref.inmemory.ChannelLayer',
#                 'ROUTING': 'live.routing.channel_routing'
#         },
# }

# Fichiers statiques (CSS, JavaScript, Images)

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Simplified static file serving HEROKU COMPRESSION GZIP
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Authentification
LOGIN_URL = reverse_lazy('index')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = LOGIN_URL
