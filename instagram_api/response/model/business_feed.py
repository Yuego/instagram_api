from instagram_api.property_mapper import PropertyMapperBase

from .summary_promotions import SummaryPromotions

__all__ = ['BusinessFeed']


class BusinessFeed(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        '_unitsgGaCa': SummaryPromotions,
    }
