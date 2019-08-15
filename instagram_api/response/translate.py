from .base_response import ApiResponse
from .model import CommentTranslations

__all__ = ['TranslateResponse']


class TranslateResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'comment_translations': [CommentTranslations],
    }
