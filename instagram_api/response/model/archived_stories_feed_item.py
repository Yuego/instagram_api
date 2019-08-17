from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['ArchivedStoriesFeedItem', 'ArchivedStoriesFeedItemInterface']


class ArchivedStoriesFeedItemInterface(ApiInterfaceBase):
    timestamp: int
    media_count: int
    id: int
    reel_type: str


class ArchivedStoriesFeedItem(PropertyMapper, ArchivedStoriesFeedItemInterface):
    pass
