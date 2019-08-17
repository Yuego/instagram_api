from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Aymf, Counts, Story, Subscription

__all__ = ['ActivityNewsResponse']


class ActivityNewsResponseInterface(ApiResponseInterface):
    new_stories: [Story]
    old_stories: [Story]
    continuation: AnyType
    friend_request_stories: [Story]
    counts: Counts
    subscription: Subscription
    partition: AnyType
    continuation_token: AnyType
    ads_manager: AnyType
    aymf: Aymf


class ActivityNewsResponse(ApiResponse, ActivityNewsResponseInterface):
    pass
