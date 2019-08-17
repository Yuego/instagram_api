from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user_card import UserCard

__all__ = ['SuggestionCard', 'SuggestionCardInterface']


class SuggestionCardInterface(ApiInterfaceBase):
    user_card: UserCard
    upsell_ci_card: AnyType
    upsell_fbc_card: AnyType


class SuggestionCard(PropertyMapper, SuggestionCardInterface):
    pass
