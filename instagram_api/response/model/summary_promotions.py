from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .business_edge import BusinessEdge
from .page_info import PageInfo

__all__ = ['SummaryPromotions', 'SummaryPromotionsInterface']


class SummaryPromotionsInterface(ApiInterfaceBase):
    edges: [BusinessEdge]
    page_info: PageInfo


class SummaryPromotions(PropertyMapper, SummaryPromotionsInterface):
    pass
