from .base_response import ApiResponse
from .model import Item, User

__all__ = ['TvChannelsResponse']


class TvChannelsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'type': str,
        'title': str,
        'id': str,
        'items': [Item],
        'more_available': bool,
        'max_id': str,
        'seen_state': None,
        'user_dict': User,
    }
