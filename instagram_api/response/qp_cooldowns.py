from .base_response import ApiResponse
from .model import QPSurface, Slot

__all__ = ['QPCooldownsResponse']


class QPCooldownsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'global': int,
        'default': int,
        'surfaces': [QPSurface],
        'slots': [Slot],
    }
