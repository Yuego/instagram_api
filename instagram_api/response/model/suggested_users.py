from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .suggestion import Suggestion
from .suggestion_card import SuggestionCard

__all__ = ['SuggestedUsers', 'SuggestedUsersInterface']


class SuggestedUsersInterface(ApiInterfaceBase):
    id: int
    view_all_text: str
    title: AnyType
    auto_dvance: str
    type: int
    tracking_token: str
    landing_site_type: str
    landing_site_title: str
    upsell_fb_pos: str
    suggestions: [Suggestion]
    suggestion_cards: [SuggestionCard]
    netego_type: str


class SuggestedUsers(PropertyMapper, SuggestedUsersInterface):
    pass
