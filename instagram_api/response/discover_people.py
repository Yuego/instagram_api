from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import SuggestedUsers

__all__ = ['DiscoverPeopleResponse']


class DiscoverPeopleResponseInterface(ApiResponseInterface):
    more_available: bool
    max_id: str
    suggested_users: SuggestedUsers
    new_suggested_users: SuggestedUsers


class DiscoverPeopleResponse(ApiResponse, DiscoverPeopleResponseInterface):
    pass
