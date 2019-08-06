from .base_response import Response
from .model import Suggestion

__all__ = ['LinkAddressBookResponse']


class LinkAddressBookResponse(Response):
    JSON_PROPERTY_MAP = {
        'items': [Suggestion],
    }
