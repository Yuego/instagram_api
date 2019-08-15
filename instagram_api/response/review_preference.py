from .base_response import ApiResponse
from .model import User

__all__ = ['ReviewPreferenceResponse']


class ReviewPreferenceResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'user': User,
    }
