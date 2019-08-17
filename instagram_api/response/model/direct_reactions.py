from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .direct_reaction import DirectReaction

__all__ = ['DirectReactions', 'DirectReactionsInterface']


class DirectReactionsInterface(ApiInterfaceBase):
    likes_count: int
    likes: [DirectReaction]


class DirectReactions(PropertyMapper, DirectReactionsInterface):
    pass
