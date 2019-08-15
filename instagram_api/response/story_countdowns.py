from .base_response import ApiResponse
from .model import CountdownSticker

__all__ = ['StoryCountdownsResponse']


class StoryCountdownsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'countdowns': [CountdownSticker],
    }
