from .base_response import Response
from .model import Hashtag

__all__ = ['TagInfoResponse']


class TagInfoResponse(Response, Hashtag):
    JSON_PROPERTY_MAP = {

    }
