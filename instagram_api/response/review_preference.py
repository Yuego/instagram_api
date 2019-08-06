from .base_response import Response
from .model import User

__all__ = ['ReviewPreferenceResponse']


class ReviewPreferenceResponse(Response):
    JSON_PROPERTY_MAP = {
        'user': User,
    }
