import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

EMAIL_HOST = 
EMAIL_PORT = 
EMAIL_USE_TLS =
EMAIL_USE_SSL =
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

INSTALLED_APPS = [   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
    'generator',
    'django_auth_ldap'
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

ROOT_URLCONF = 'settings.urls'

SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_SECONDS = 7200
SESSION_TIMEOUT_REDIRECT = '/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'static'),
            os.path.join(BASE_DIR, 'media'),
        ],
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

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.tz",
  "django.contrib.messages.context_processors.messages",
  "myproject.context_processors.sidebar_articles",
  
)

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbppr',
        'HOST': '127.0.0.1',
        'PORT': '3310',  
        'USER': 'root',
        'PASSWORD': 'CM@2019ti',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATE_INPUT_FORMATS = ('%d-%m-%Y')

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

# Configura????o de log do console. N??o alterar.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}},
}

# URL do servidor padr??o. Abra o CMD e digite o comando: nslookup.
AUTH_LDAP_SERVER_URI = ""

# Usu??rio e senha do BIND. Aconselho um usu??rio de servi??o 24h com acesso full para search.
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""

# M??todos de pesquisa para usu??rios e grupos. Podem ser a mesma queryset para ambos mas aconselho criar um grupo de acesso dentro do AD para os usu??rio que ir??o acessar a plataforma.
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=,ou=,dc=,dc=,dc=", ldap.SCOPE_SUBTREE, "(samaccountname=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=,ou=,dc=,dc=,dc=", ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)")

# Configura????o padr??o para tipos de grupo. N??o alterar.
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# Configura????o padr??o para alimenta????o do banco da aplica????o. N??o alterar
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name" : "sn",
    "email"     : "mail",
}

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)
