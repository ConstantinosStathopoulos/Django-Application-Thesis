"""
Django settings for hua_thesis project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import ldap
from decouple import config
from django_auth_ldap.config import LDAPSearch, LDAPGroupQuery, GroupOfNamesType
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAT=os.path.join(BASE_DIR,'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    
    #my apps
    'accounts.apps.AccountsConfig',
    'hua_thesis',
    'student.apps.StudentConfig',
    'professor.apps.ProfessorConfig',
    'office.apps.OfficeConfig'
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

ROOT_URLCONF = 'hua_thesis.urls'

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

WSGI_APPLICATION = 'hua_thesis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#Default setup for intergrated sqlite db
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
#     }
# }

#Connect to PostgreSQL database(hosted on heroku)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config('DB_NAME'),
        "USER": config('DB_USERNAME'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT', cast=int),
    }
}


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#SMTP Configuration / Email settings
# EMAIL_BACKEND = config('EMAIL_BACKEND')
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# EMAI_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')







#Ldap Settings

#LDAP connection parameters
AUTH_LDAP_SERVER_URI = config('AUTH_LDAP_SERVER_URI')
AUTH_LDAP_BIND_DN = config('AUTH_LDAP_BIND_DN')
AUTH_LDAP_BIND_PASSWORD = config('AUTH_LDAP_BIND_PASSWORD')
AUTH_LDAP_START_TLS = True
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=hua,dc=gr", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)

#LDAP group to search for user
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "ou=Groups,dc=hua,dc=gr", ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

AUTH_LDAP_MIRROR_GROUPS = True  # Will sync ldap groups to django, if not exist

## ! My test users do not belong in ou=Groups.
#Allow only users of specific groups(e.g deny login of undergrad students)
# AUTH_LDAP_REQUIRE_GROUP = (
#     LDAPGroupQuery("cn=pos_dit,ou=Groups,dc=hua,dc=gr")
#     | LDAPGroupQuery("cn=pos_die,ou=Groups,dc=hua,dc=gr")
#     | LDAPGroupQuery("cn=pos_eco,ou=Groups,dc=hua,dc=gr")
#     | LDAPGroupQuery("cn=pos_geo,ou=Groups,dc=hua,dc=gr")
# ) 
## ? I will try to limit access with deny_group, until the testing users are in the apropriate groups
# AUTH_LDAP_DENY_GROUP = (
#     LDAPGroupQuery("cn=und_die,ou=Groups,dc=hua,dc=gr")
#     # | LDAPGroupQuery("cn=und_dit,ou=Groups,dc=hua,dc=gr")
#     | LDAPGroupQuery("cn=und_eco,ou=Groups,dc=hua,dc=gr")
#     | LDAPGroupQuery("cn=und_geo,ou=Groups,dc=hua,dc=gr")
# )


#Grouping of LDAP users.

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": ("cd="),
#     "is_staff": (
#         LDAPGroupQuery("cn=administrative,ou=Groups,dc=hua,dc=gr")),
# }

#Attributes from LDAP
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName", 
    "last_name": "sn", 
    "email" : "email",
    "department" : "schacPersonalPosition",
    "title" : "title",
    }
AUTH_LDAP_BASE_DN = 'dc=hua,dc=gr'

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_MIRROR_GROUPS = True
# Cache names and group memberships for an hour to minimize LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#login redirect
LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Media files(e.g pdf receipts of payments)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'


STATICFILES_DIRS = (
    "hua_thesis/static/static/",
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)