from instagram_api.property_mapper import PropertyMapperBase

from .eligible_promotions import EligiblePromotions

__all__ = ['Viewer']


class Viewer(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'eligible_promotions': EligiblePromotions,
    }
