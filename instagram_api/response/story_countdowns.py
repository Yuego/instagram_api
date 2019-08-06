from .base_response import Response
from .model import CountdownSticker

__all__ = ['StoryCountdownsResponse']


class StoryCountdownsResponse(Response):
    JSON_PROPERTY_MAP = {
        'countdowns': [CountdownSticker],
    }
