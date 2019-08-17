from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Related', 'RelatedInterface']


class RelatedInterface(ApiInterfaceBase):
    name: AnyType
    id: int
    type: AnyType


class Related(PropertyMapper, RelatedInterface):
    pass
