from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .chaining_info import ChainingInfo

__all__ = ['ChainingSuggestion', 'ChainingSuggestionInterface']


class ChainingSuggestionInterface(ApiInterfaceBase):
    chaining_info: ChainingInfo
    profile_chaining_secondary_label: AnyType


class ChainingSuggestion(PropertyMapper, ChainingSuggestionInterface):
    pass
