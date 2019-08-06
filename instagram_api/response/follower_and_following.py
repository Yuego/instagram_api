from .base_response import Response
from .model import SuggestedUsers, User

__all__ = ['FollowerAndFollowingResponse']


class FollowerAndFollowingResponse(Response):
    JSON_PROPERTY_MAP = {
        'users': [User],
        'suggested_users': SuggestedUsers,
        'truncate_follow_requests_at_index': int,
        'next_max_id': str,
        'page_size': None,
        'big_list': bool,
    }