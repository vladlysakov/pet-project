from django.contrib.auth import authenticate
from jwt import DecodeError, get_unverified_header, decode
from jwt.algorithms import RSAAlgorithm
from pydash import get
from rest_framework_jwt.settings import api_settings


def get_username_from_payload_handler(payload: dict) -> str:
    username: str = get(payload, 'sub')
    authenticate(remote_user=username)

    return username


def cognito_jwt_decode_handler(token: str):
    options = {'verify_exp': True}

    unverified_header = get_unverified_header(token)

    if 'kid' not in unverified_header:
        raise DecodeError('Incorrect authentication credentials.')

    kid = get(unverified_header, 'token.kid')

    try:
        public_key = RSAAlgorithm.from_jwk(api_settings.JWT_PUBLIC_KEY[kid])
    except KeyError:
        raise DecodeError('Can\'t find proper public key in jwks')

    return decode(
        token,
        public_key,
        api_settings.JWT_VERIFY,
        options=options,
        audience=api_settings.JWT_AUDIENCE,
        issuer=api_settings.JWT_ISSUER,
        algorithms=[api_settings.JWT_ALGORITHM]
    )
