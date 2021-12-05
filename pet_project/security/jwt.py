from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken


class CognitoToken(AccessToken):
    token_type = 'id'

    def get_token_backend(self):
        self._token_backend = super().get_token_backend()
        self._token_backend.jwk_url = api_settings.JWK_URL

        return self._token_backend
