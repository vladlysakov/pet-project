import os

from pet_project.common.constants import JWTVariables
from pet_project.security.utils import get_aws_keys


class CognitoConfig:
    header_prefix = os.getenv(JWTVariables.HEADER_PREFIX, JWTVariables.DEFAULT_HEADER_PREFIX)
    user_pool_id = os.getenv(JWTVariables.AWS_COGNITO_USER_POOL)
    app_client_ids = os.getenv(JWTVariables.AWS_COGNITO_CLIENT_ID)
    algorithm = os.getenv(JWTVariables.ALGORITHM, JWTVariables.DEFAULT_ALGORITHM)
    region = os.getenv(JWTVariables.AWS_REGION, JWTVariables.DEFAULT_AWS_REGION)

    issuer = f'https://cognito-idp.{region}.amazonaws.com/{user_pool_id}'
    keys_url = f'{issuer}/.well-known/jwks.json'

    keys = get_aws_keys(keys_url)
