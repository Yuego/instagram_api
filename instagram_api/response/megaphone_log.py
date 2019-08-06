from .base_response import Response

__all__ = ['MegaphoneLogResponse']


class MegaphoneLogResponse(Response):
    JSON_PROPERTY_MAP = {
        'success': None,
    }
