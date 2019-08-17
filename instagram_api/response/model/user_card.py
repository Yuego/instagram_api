from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['UserCard', 'UserCardInterface']


class UserCardInterface(ApiInterfaceBase):
    user: User
    algorithm: str
    social_context: str
    caption: AnyType
    icon: AnyType
    media_ids: AnyType
    thumbnail_urls: AnyType
    large_urls: AnyType
    media_infos: AnyType
    value: float
    is_new_suggestion: bool
    uuid: str
    followed_by: bool


class UserCard(PropertyMapper, UserCardInterface):
    pass
