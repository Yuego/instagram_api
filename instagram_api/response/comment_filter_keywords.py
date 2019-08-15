from .base_response import ApiResponse

__all__ = ['CommentFilterKeywordsResponse']


class CommentFilterKeywordsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'keywords': None,
    }
