from .base_response import Response
from .model import StoryTray

__all__ = ['LocationStoryResponse']


class LocationStoryResponse(Response):
    JSON_PROPERTY_MAP = {
        'story': StoryTray,
    }
