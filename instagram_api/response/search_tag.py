from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Tag

__all__ = ['SearchTagResponse']


class SearchTagResponseInterface(ApiResponseInterface):
    has_more: bool
    results: [Tag]
    rank_token: str


class SearchTagResponse(ApiResponse, SearchTagResponseInterface):
    pass
