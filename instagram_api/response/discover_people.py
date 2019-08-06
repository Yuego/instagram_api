from .base_response import Response
from .model import SuggestedUsers

__all__ = ['DiscoverPeopleResponse']


class DiscoverPeopleResponse(Response):
    JSON_PROPERTY_MAP = {
        'more_available': bool,
        'max_id': str,
        'suggested_users': SuggestedUsers,
        'new_suggested_users': SuggestedUsers,
    }
