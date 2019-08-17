from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .location_item import LocationItem
from .hashtag import Hashtag
from .user import User

__all__ = ['Suggested', 'SuggestedInterface']


class SuggestedInterface(ApiInterfaceBase):
    position: int
    hashtag: Hashtag
    user: User
    place: LocationItem
    client_time: AnyType


class Suggested(PropertyMapper, SuggestedInterface):
    pass
