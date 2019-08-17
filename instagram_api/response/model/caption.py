from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Caption', 'CaptionInterface']


class CaptionInterface(ApiInterfaceBase):
    status: str
    user_id: int
    created_at_utc: str
    created_at: str
    bit_flags: int
    user: User
    content_type: AnyType
    text: str
    media_id: int
    pk: int
    type: int
    has_translation: bool
    did_report_as_spam: bool
    share_enabled: bool


class Caption(PropertyMapper, CaptionInterface):
    pass
