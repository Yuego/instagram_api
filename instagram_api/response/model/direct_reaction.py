from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType


__all__ = ['DirectReaction', 'DirectReactionInterface']


class DirectReactionInterface(ApiInterfaceBase):
    reaction_type: str
    timestamp: Timestamp
    sender_id: int
    client_context: str
    reaction_status: str
    node_type: str
    item_id: int


class DirectReaction(PropertyMapper, DirectReactionInterface):
    pass
