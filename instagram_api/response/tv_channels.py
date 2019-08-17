from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item, User

__all__ = ['TvChannelsResponse']


class TvChannelsResponseInterface(ApiResponseInterface):
    type: str
    title: str
    id: str
    items: [Item]
    more_available: bool
    max_id: str
    seen_state: AnyType
    user_dict: User


class TvChannelsResponse(ApiResponse, TvChannelsResponseInterface):
    pass
