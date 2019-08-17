from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Hashtag', 'HashtagInterface']


class HashtagInterface(ApiInterfaceBase):
    id: int
    name: str
    media_count: int
    profile_pic_url: str
    follow_status: int
    following: int
    allow_following: int
    allow_muting_story: bool
    related_tags: AnyType
    debug_info: AnyType


class Hashtag(PropertyMapper, HashtagInterface):
    pass

