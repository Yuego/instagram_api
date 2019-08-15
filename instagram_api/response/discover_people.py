from .base_response import ApiResponse
from .model import SuggestedUsers

__all__ = ['DiscoverPeopleResponse']


class DiscoverPeopleResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'more_available': bool,
        'max_id': str,
        'suggested_users': SuggestedUsers,
        'new_suggested_users': SuggestedUsers,
    }
