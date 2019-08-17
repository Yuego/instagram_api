from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .summary_promotions import SummaryPromotions

__all__ = ['PromotionsUnit', 'PromotionsUnitInterface']


class PromotionsUnitInterface(ApiInterfaceBase):
    _summary_promotions2ubm1F: SummaryPromotions


class PromotionsUnit(PropertyMapper, PromotionsUnitInterface):
    pass
