from .base_response import Response

__all__ = ['CommentCategoryFilterResponse']


class CommentCategoryFilterResponse(Response):
    JSON_PROPERTY_MAP = {
        'disabled': None,
    }
