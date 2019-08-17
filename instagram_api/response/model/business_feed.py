from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .summary_promotions import SummaryPromotions

__all__ = ['BusinessFeed', 'BusinessFeedInterface']


class BusinessFeedInterface(ApiInterfaceBase):
    _unitsgGaCa: SummaryPromotions


class BusinessFeed(PropertyMapper, BusinessFeedInterface):
    pass
