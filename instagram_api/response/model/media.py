from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Media', 'MediaInterface']


class MediaInterface(ApiInterfaceBase):
    image: str
    id: int
    user: User
    expiring_at: Timestamp
    comment_threading_enabled: bool


class Media(PropertyMapper, MediaInterface):
    pass
