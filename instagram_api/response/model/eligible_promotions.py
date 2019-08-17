from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .edges import Edges

__all__ = ['EligiblePromotions', 'EligiblePromotionsInterface']


class EligiblePromotionsInterface(ApiInterfaceBase):
    edges: [Edges]


class EligiblePromotions(PropertyMapper, EligiblePromotionsInterface):
    pass
