from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Counts', 'CountsInterface']


class CountsInterface(ApiInterfaceBase):
    relationships: AnyType
    requests: AnyType
    photos_of_you: AnyType
    usertags: AnyType
    comments: AnyType
    likes: AnyType
    comment_likes: AnyType
    campaign_notification: AnyType


class Counts(PropertyMapper, CountsInterface):
    pass

