from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import User

__all__ = ['ViewerListResponse']


class ViewerListResponseInterface(ApiResponseInterface):
    users: [User]


class ViewerListResponse(ApiResponse, ViewerListResponseInterface):
    pass
