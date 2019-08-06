from .base_response import Response
from .model import User

__all__ = ['ViewerListResponse']


class ViewerListResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
    }
