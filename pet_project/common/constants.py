class EnvironmentVariables:
    DEFAULT_RETRIES_LIMIT = 3


class JWTVariables:
    # PUBLIC_KEY = ''
    HEADER_PREFIX = 'JWT_HEADER_PREFIX'
    DEFAULT_HEADER_PREFIX = 'Bearer',

    ALGORITHM = 'ALGORITHM'
    DEFAULT_ALGORITHM = 'RS256'

    AWS_REGION = 'AWS_REGION'
    DEFAULT_AWS_REGION = 'eu-west-2'

    AWS_COGNITO_USER_POOL = 'AWS_COGNITO_USER_POOL'
    AWS_COGNITO_CLIENT_ID = 'AWS_COGNITO_CLIENT_ID'
    # AUDIENCE = ''
    # ISSUER = ''


class KeysVariables:
    SECRET_KEY = 'SECRET_KEY'
    SECRET_KEY_VALUE = 'django-insecure-wve!il9uq4kv!zo&f%-et+283y-$(gov-w4f+hq=+2c@w_ajz$'


class AllowedHostsVariables:
    DEFAULT_HOST_NUMBER = '0.0.0.0'
    DEFAULT_HOST_NAME = 'localhost'

    ALL = DEFAULT_HOST_NUMBER, DEFAULT_HOST_NAME


class DatabaseVariables:
    ENGINE = 'ENGINE'
    DEFAULT_ENGINE = 'django.db.backends.postgresql'

    HOST = 'HOST'
    DEFAULT_HOST = 'localhost'

    PORT = 'PORT'
    DEFAULT_PORT = 5432

    TABLE = 'NAME'
    DEFAULT_TABLE_NAME = 'diploma'

    USER = 'DATABASE_USER'
    DEFAULT_USER = 'postgres'

    PASSWORD = 'PASSWORD'
    DEFAULT_PASSWORD = '1'

    AUTH_USER_MODEL = 'AUTH_USER_MODEL'
    DEFAULT_AUTH_USER_MODEL = 'user.User'


class DecodeConstants:
    UTF8 = 'utf-8'
