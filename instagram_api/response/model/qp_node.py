from instagram_api.property_mapper import PropertyMapperBase

from .contextual_filters import ContextualFilters
from .creative import Creative
from .template import Template

__all__ = ['QPNode']


class QPNode(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'promotion_id': int,
        'max_impressions': int,
        'triggers': [str],
        'contextual_filters': ContextualFilters,
        'template': Template,
        'creatives': [Creative],
    }
