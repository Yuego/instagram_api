from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['BlockedReels', 'BlockedReelsInterface']


class BlockedReelsInterface(ApiInterfaceBase):
    users: [User]
    page_size: AnyType
    big_list: bool


class BlockedReels(PropertyMapper, BlockedReelsInterface):
    pass
