from .base_response import Response
from .model import CommentTranslations

__all__ = ['TranslateResponse']


class TranslateResponse(Response):
    JSON_PROPERTY_MAP = {
        'comment_translations': [CommentTranslations],
    }
