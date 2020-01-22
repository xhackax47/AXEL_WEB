import hashlib
import os
import sys
import random
import string

import sentry_sdk
from django.conf.global_settings import ADMINS
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DEBUG = True pour le mode Développement
# DEBUG = False pour le mode Production
DEBUG = False
NOT_TEST = eval("'test' not in sys.argv or 'test_coverage' in sys.argv")

env_vars = [
    'ADMIN',
    'DB_HOST',
    'DB_NAME',
    'DB_USER',
    'DB_PASSWORD',
    'EMAIL_BACKEND',
    'EMAIL_HOST',
    'EMAIL_HOST_PASSWORD',
    'EMAIL_HOST_USER',
    'EMAIL_PORT',
    'GOOGLE_RECAPTCHA_SECRET_KEY',
    'MANAGERS',
    'SECRET_KEY',
]

# PRODUCTION : On met toutes les variables dans un tableau settings
settings = {}
if not DEBUG and NOT_TEST:
    for var in env_vars:
        try:
            settings[var] = os.environ[var]
        except KeyError as ke:
            print(_(f'ATTENTION la variable d\'environnement {var} n\'a pas été trouvé'))
            settings[var] = 'ko'

# Initialisation Sentry Montoring
sentry_sdk.init(
    dsn="https://38fa4be46e8c4295b2ec9bda26b4b232@sentry.io/1887341",
    integrations=[DjangoIntegration()],

    # Associer les utilisateurs aux erreurs
    send_default_pii=True
)

# Clé secrète selon l'environnement
if DEBUG and NOT_TEST:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'c@n%u@91tum=@j392g20b8znh7dqfo-v%81))gxbbmu$=dy_*)')
elif not DEBUG and NOT_TEST:
    SECRET_KEY = settings['SECRET_KEY']
else:
    SECRET_KEY = '1hewzbdd-rb*+r)r2u&ewfp90s9gy&lmc35j!38wtis8r6ze4k'

# Hôtes autorisés selon l'environnement
if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['axel-ihm.herokuapp.com']

# Configuration sécurité SSL et cookies
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# reCaptcha Google
if not DEBUG and NOT_TEST:
    GOOGLE_RECAPTCHA_SECRET_KEY = settings['GOOGLE_RECAPTCHA_SECRET_KEY']

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

# Utilisateur et groupes personnalisés
AUTH_USER_MODEL = 'WebAXEL.AxelUser'
AUTH_GROUP_MODEL = 'WebAXEL.AxelGroup'

# Framework Web à utiliser avec crispy
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

if not DEBUG and NOT_TEST:
    ADMIN = settings['ADMIN']
    MANAGERS = settings['MANAGERS']
    ROOT_URLCONF = 'AXEL_WEB.urls'

# Configuration email pour l'activation de comptes
if not DEBUG and NOT_TEST:
    EMAIL_BACKEND = settings['EMAIL_BACKEND']
    EMAIL_USE_TLS = True
    EMAIL_HOST = settings['EMAIL_HOST']
    EMAIL_HOST_USER = settings['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = settings['EMAIL_HOST_PASSWORD']
    EMAIL_PORT = settings['EMAIL_PORT']

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
if not DEBUG and NOT_TEST:
    # Configuration BDD PostgreSQL Distante en mode Production (DEBUG=False)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': settings['DB_NAME'],
            'USER': settings['DB_USER'],
            'PASSWORD': settings['DB_PASSWORD'],
            'HOST': settings['DB_HOST'],
            'PORT': '5432',
        }
    }
elif DEBUG and NOT_TEST:
    # Configuration BDD PostgreSQL Local en mode Développement (DEBUG=TRUE)
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

# Configuration BDD SQLITE pour tests et Intégration Continue CircleCI
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

# Chemin des fichiers de traductions
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'static/locale/'),
)
gettext = lambda x: x

# Langages pris en charge par la traduction
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
    # Fichiers statiques en mode Développement
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
else:
    # Fichiers statiques en mode Production
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Simplified static file serving HEROKU COMPRESSION GZIP
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Authentification
LOGIN_URL = reverse_lazy('index')
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = LOGIN_URL
