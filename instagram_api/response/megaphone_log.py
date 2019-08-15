from .base_response import ApiResponse

__all__ = ['MegaphoneLogResponse']


class MegaphoneLogResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'success': None,
    }
