from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CommentFilterKeywordsResponse']


class CommentFilterKeywordsResponseInterface(ApiResponseInterface):
    keywords: AnyType


class CommentFilterKeywordsResponse(ApiResponse, CommentFilterKeywordsResponseInterface):
    pass
