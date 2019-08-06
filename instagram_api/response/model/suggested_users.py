from instagram_api.property_mapper import PropertyMapperBase

from .suggestion import Suggestion
from .suggestion_card import SuggestionCard

__all__ = ['SuggestedUsers']


class SuggestedUsers(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'view_all_text': str,
        'title': None,
        'auto_dvance': str,
        'type': int,
        'tracking_token': str,
        'landing_site_type': str,
        'landing_site_title': str,
        'upsell_fb_pos': str,
        'suggestions': [Suggestion],
        'suggestion_cards': [SuggestionCard],
        'netego_type': str,
    }
