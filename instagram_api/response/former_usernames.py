from .base_response import ApiResponse
from .model import FormerUsername

__all__ = ['FormerUsernamesResponse']


class FormerUsernamesResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'former_usernames': [FormerUsername],
    }
