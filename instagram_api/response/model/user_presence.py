from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['UserPresence', 'UserPresenceInterface']


class UserPresenceInterface(ApiInterfaceBase):
    user_id: int
    last_activity_at_ms: str
    is_active: bool
    in_threads: [str]


class UserPresence(PropertyMapper, UserPresenceInterface):
    pass
