from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item

__all__ = ['EditMediaResponse']


class EditMediaResponseInterface(ApiResponseInterface):
    media: Item


class EditMediaResponse(ApiResponse, EditMediaResponseInterface):
    pass
