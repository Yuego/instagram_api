from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['BiographyEntities', 'BiographyEntitiesInterface']


class BiographyEntitiesInterface(ApiInterfaceBase):
    entities: AnyType
    raw_text: str
    nux_type: str


class BiographyEntities(PropertyMapper, BiographyEntitiesInterface):
    pass
