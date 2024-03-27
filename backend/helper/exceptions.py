from rest_framework import status
from rest_framework.exceptions import APIException


class TokenNotProvided(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Token not present in header."
    default_code = "token_error"


class TokenExpired(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Token expired."
    default_code = "token_expired"


class InvalidToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid Token."
    default_code = "invalid_token"


class TokenFornatException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Token Format invalid."
    default_code = "token_format_invalid"
