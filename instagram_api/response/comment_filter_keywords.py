from .base_response import Response

__all__ = ['CommentFilterKeywordsResponse']


class CommentFilterKeywordsResponse(Response):
    JSON_PROPERTY_MAP = {
        'keywords': None,
    }
