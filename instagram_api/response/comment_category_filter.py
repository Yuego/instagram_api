from .base_response import ApiResponse

__all__ = ['CommentCategoryFilterResponse']


class CommentCategoryFilterResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'disabled': None,
    }
