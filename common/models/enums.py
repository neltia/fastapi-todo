from enum import Enum


class ResponseCodeEnum(int, Enum):
    SUCCESS = 200

    INVALID_PARAM = 400
    UNAUTHORIZED = 401
    NO_AUTHORITY_TO_USE = 403
    NOT_FOUND = 404

    SERVER_ERROR = 500
