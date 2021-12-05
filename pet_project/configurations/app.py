import os

from pet_project.common.constants import KeysVariables


class SecretKeyConfig:
    key = os.getenv(KeysVariables.SECRET_KEY, KeysVariables.SECRET_KEY_VALUE)
