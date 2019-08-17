from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import CommentTranslations

__all__ = ['TranslateResponse']


class TranslateResponseInterface(ApiResponseInterface):
    comment_translations: [CommentTranslations]


class TranslateResponse(ApiResponse, TranslateResponseInterface):
    pass
