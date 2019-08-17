from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['HiddenEntities', 'HiddenEntitiesInterface']


class HiddenEntitiesInterface(ApiInterfaceBase):
    user: AnyType
    hashtag: AnyType
    place: AnyType


class HiddenEntities(PropertyMapper, HiddenEntitiesInterface):
    pass
