from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Attribution', 'AttributionInterface']


class AttributionInterface(ApiInterfaceBase):
    name: str


class Attribution(PropertyMapper, AttributionInterface):
    pass
