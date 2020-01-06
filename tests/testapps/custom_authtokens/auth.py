from rest_framework.authentication import BaseAuthentication

from rest_registration.auth_token_managers import AbstractAuthTokenManager
from rest_registration.exceptions import (
    AuthTokenNotProvided,
    AuthTokenNotRevoked
)


class FaultyAuthTokenManager(AbstractAuthTokenManager):

    def get_authentication_class(self):
        return BaseAuthentication

    def provide_token(self, user):
        raise AuthTokenNotProvided()

    def revoke_token(self, user, *, token=None):
        raise AuthTokenNotRevoked()
