from .base_response import ApiResponse

__all__ = ['BlockedMediaResponse']


class BlockedMediaResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'media_ids': None,
    }
