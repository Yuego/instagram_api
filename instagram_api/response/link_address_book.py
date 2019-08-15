from .base_response import ApiResponse
from .model import Suggestion

__all__ = ['LinkAddressBookResponse']


class LinkAddressBookResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'items': [Suggestion],
    }
