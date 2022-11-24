import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-suxs$x4m#_a$xei2z38--t=5aah3g&awm#7zxx)7hf4bt^-#=&'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

EMAIL_HOST = 'notesserver.colorado.com.br'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
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

# Configuração de log do console. Não alterar.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}},
}

# URL do servidor padrão. Abra o CMD e digite o comando: nslookup.
AUTH_LDAP_SERVER_URI = "ldap://COLWAD01.coloradomaq.com.br"

# Usuário e senha do BIND. Aconselho um usuário de serviço 24h com acesso full para search.
AUTH_LDAP_BIND_DN = "cn=Gustavo Lisi Dias,ou=TI,ou=Usuários,ou=Colorado Maquinas,dc=coloradomaq,dc=com,dc=br"
AUTH_LDAP_BIND_PASSWORD = "CM@2019ti"

# Métodos de pesquisa para usuários e grupos. Podem ser a mesma queryset para ambos mas aconselho criar um grupo de acesso dentro do AD para os usuário que irão acessar a plataforma.
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Usuários,ou=Colorado Maquinas,dc=coloradomaq,dc=com,dc=br", ldap.SCOPE_SUBTREE, "(samaccountname=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Usuários,ou=Colorado Maquinas,dc=coloradomaq,dc=com,dc=br", ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)")

# Configuração padrão para tipos de grupo. Não alterar.
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# Configuração padrão para alimentação do banco da aplicação. Não alterar
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name" : "sn",
    "email"     : "mail",
}

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)