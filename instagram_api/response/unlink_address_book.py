from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['UnlinkAddressBookResponse']


class UnlinkAddressBookResponseInterface(ApiResponseInterface):
    pass


class UnlinkAddressBookResponse(ApiResponse, UnlinkAddressBookResponseInterface):
    pass
