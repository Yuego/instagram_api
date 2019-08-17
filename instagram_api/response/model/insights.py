from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Insights', 'InsightsInterface']


class InsightsInterface(ApiInterfaceBase):
    instagram_insights: AnyType


class Insights(PropertyMapper, InsightsInterface):
    pass
