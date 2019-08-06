from .base_response import Response

__all__ = ['BlockedMediaResponse']


class BlockedMediaResponse(Response):
    JSON_PROPERTY_MAP = {
        'media_ids': None,
    }
