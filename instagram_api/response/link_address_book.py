from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Suggestion

__all__ = ['LinkAddressBookResponse']


class LinkAddressBookResponseInterface(ApiResponseInterface):
    items: [Suggestion]


class LinkAddressBookResponse(ApiResponse, LinkAddressBookResponseInterface):
    pass
