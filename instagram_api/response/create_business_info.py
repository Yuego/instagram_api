from .mapper import ApiResponse, ApiResponseInterface

from .model import User

__all__ = ['CreateBusinessInfoResponse']


class CreateBusinessInfoResponseInterface(ApiResponseInterface):
    users: [User]


class CreateBusinessInfoResponse(ApiResponse, CreateBusinessInfoResponseInterface):
    pass
