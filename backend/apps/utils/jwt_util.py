import jwt
from rest_framework.authentication import BaseAuthentication

from backend import settings
from backend.helper.exceptions import (
    InvalidToken,
    TokenExpired,
    TokenFornatException,
    TokenNotProvided,
)


class JWTAuthentication(BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user id and token. If not, throw an error.
        """
        authorization_header = request.headers.get("Authorization")

        if not authorization_header:
            # raise TokenFornatException(f'Access token must be in the format '
            # f'<{self.keyword} access_token>')
            return None

        try:
            authorization_header = authorization_header.split(" ")
            if authorization_header[0] != self.keyword:
                return None
            elif len(authorization_header) != 2:
                raise TokenFornatException(
                    f"Access token must be in the format "
                    f"<{self.keyword} access_token>"
                )

            access_token = authorization_header[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError as e:
            raise TokenExpired()
        except Exception as e:
            raise InvalidToken("Invalid access token")

        return payload["user_id"], access_token
