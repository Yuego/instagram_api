from instagram_api.property_mapper import PropertyMapperBase

from .summary_promotions import SummaryPromotions

__all__ = ['PromotionsUnit']


class PromotionsUnit(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        '_summary_promotions2ubm1F': SummaryPromotions,
    }
