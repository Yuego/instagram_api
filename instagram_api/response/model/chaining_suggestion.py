from instagram_api.property_mapper import PropertyMapperBase

from .chaining_info import ChainingInfo

__all__ = ['ChainingSuggestion']


class ChainingSuggestion(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'chaining_info': ChainingInfo,
        'profile_chaining_secondary_label': None,
    }
