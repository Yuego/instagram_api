from instagram_api.property_mapper import PropertyMapperBase

from .user_card import UserCard

__all__ = ['SuggestionCard']


class SuggestionCard(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'user_card': UserCard,
        'upsell_ci_card': None,
        'upsell_fbc_card': None,
    }
