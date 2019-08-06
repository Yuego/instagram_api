from .base_response import Response
from .model import Aymf, Counts, Story, Subscription

__all__ = ['ActivityNewsResponse']


class ActivityNewsResponse(Response):
    JSON_PROPERTY_MAP = {
        'new_stories': [Story],
        'old_stories': [Story],
        'continuation': None,
        'friend_request_stories': [Story],
        'counts': Counts,
        'subscription': Subscription,
        'partition': None,
        'continuation_token': None,
        'ads_manager': None,
        'aymf': Aymf,
    }