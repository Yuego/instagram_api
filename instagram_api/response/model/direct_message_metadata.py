from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType


__all__ = ['DirectMessageMetadata', 'DirectMessageMetadataInterface']


class DirectMessageMetadataInterface(ApiInterfaceBase):
    thread_id: int
    item_id: int
    timestamp: Timestamp
    participant_ids: [int]


class DirectMessageMetadata(PropertyMapper, DirectMessageMetadataInterface):
    pass
