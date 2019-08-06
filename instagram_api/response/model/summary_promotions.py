from instagram_api.property_mapper import PropertyMapperBase

from .business_edge import BusinessEdge
from .page_info import PageInfo

__all__ = ['SummaryPromotions']


class SummaryPromotions(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'edges': [BusinessEdge],
        'page_info': PageInfo,
    }
