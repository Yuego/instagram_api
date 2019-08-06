from .base_response import Response
from .model import QPSurface, Slot

__all__ = ['QPCooldownsResponse']


class QPCooldownsResponse(Response):
    JSON_PROPERTY_MAP = {
        'global': int,
        'default': int,
        'surfaces': [QPSurface],
        'slots': [Slot],
    }
