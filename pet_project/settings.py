from datetime import timedelta
from pathlib import Path

from pet_project.common.constants import AllowedHostsVariables
from pet_project.configurations.app import SecretKeyConfig
from pet_project.configurations.cognito import CognitoConfig
from pet_project.configurations.database import DatabaseConfig

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SecretKeyConfig.key

DEBUG = True
CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = AllowedHostsVariables.ALL

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt'
]

CUSTOM_APPLICATIONS = 'user.apps.UserConfig',

INSTALLED_APPS += CUSTOM_APPLICATIONS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'pet_project.urls'

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

WSGI_APPLICATION = 'pet_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': DatabaseConfig.engine,
        'NAME': DatabaseConfig.name,
        'USER': DatabaseConfig.user,
        'PASSWORD': DatabaseConfig.password,
        'HOST': DatabaseConfig.host,
        'PORT': DatabaseConfig.port,
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': 'pet_project.security.permissions.DenyAny',
}

SIMPLE_JWT = {
    'UPDATE_LAST_LOGIN': True,
    'VERIFYING_KEY': CognitoConfig.keys,
    'ALGORITHM': CognitoConfig.algorithm,
    'AUDIENCE': CognitoConfig.app_client_ids.split(),
    'JWK_URL': CognitoConfig.keys_url,
    'ISSUER': CognitoConfig.issuer,
    'JTI_CLAIM': 'event_id',
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'TOKEN_TYPE_CLAIM': 'token_use',
    'USER_ID_CLAIM': 'sub',
    'USER_ID_FIELD': 'uuid',
    'AUTH_TOKEN_CLASSES': ('pet_project.security.jwt.CognitoToken',),
}

AUTH_USER_MODEL = DatabaseConfig.user_model

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
