from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AdMetadata', 'AdMetadataInterface']


class AdMetadataInterface(ApiInterfaceBase):
    value: AnyType
    type: AnyType


class AdMetadata(PropertyMapper, AdMetadataInterface):
    pass
