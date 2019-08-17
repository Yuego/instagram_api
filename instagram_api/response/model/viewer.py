from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .eligible_promotions import EligiblePromotions

__all__ = ['Viewer', 'ViewerInterface']


class ViewerInterface(ApiInterfaceBase):
    eligible_promotions: EligiblePromotions


class Viewer(PropertyMapper, ViewerInterface):
    pass
