from .base_response import Response
from .model import User

__all__ = ['BroadcastJoinRequestCountResponse']


class BroadcastJoinRequestCountResponse(Response):
    JSON_PROPERTY_MAP = {
        'fetch_ts': int,
        'num_total_requests': int,
        'num_new_requests': int,
        'users': [User],
        'num_unseen_requests': int,
    }
