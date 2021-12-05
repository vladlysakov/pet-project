import urllib.request
from json import loads

from pydash import get

from pet_project.common.constants import DecodeConstants


def get_aws_keys(keys_url):
    with urllib.request.urlopen(keys_url) as cognito_response:
        response_body = cognito_response.read()

    json_response = loads(response_body.decode(DecodeConstants.UTF8))
    keys = get(json_response, 'keys')

    return keys
