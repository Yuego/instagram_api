from .base_response import ApiResponse
from .model import Hashtag

__all__ = ['TagInfoResponse']


class TagInfoResponse(ApiResponse, Hashtag):
    JSON_PROPERTY_MAP = {

    }
