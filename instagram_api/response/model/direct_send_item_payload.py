from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType


__all__ = ['DirectSendItemPayload', 'DirectSendItemPayloadInterface']


class DirectSendItemPayloadInterface(ApiInterfaceBase):
    client_request_id: int
    client_context: str
    message: str
    item_id: int
    timestamp: Timestamp
    thread_id: int
    canonical: bool
    participant_ids: [int]


class DirectSendItemPayload(PropertyMapper, DirectSendItemPayloadInterface):
    pass
