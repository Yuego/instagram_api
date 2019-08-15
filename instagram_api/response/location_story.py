from .base_response import ApiResponse
from .model import StoryTray

__all__ = ['LocationStoryResponse']


class LocationStoryResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'story': StoryTray,
    }
