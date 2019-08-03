from instagram_api.property_mapper import PropertyMapperBase

from .edges import Edges

__all__ = ['EligiblePromotions']


class EligiblePromotions(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'edges': [Edges],
    }
