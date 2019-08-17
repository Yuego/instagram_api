from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Headline', 'HeadlineInterface']


class HeadlineInterface(ApiInterfaceBase):
    content_type: AnyType
    user: User
    user_id: int
    pk: str
    text: str
    type: AnyType
    created_at: Timestamp
    created_at_utc: str
    media_id: int
    bit_flags: int
    status: AnyType


class Headline(PropertyMapper, HeadlineInterface):
    pass
