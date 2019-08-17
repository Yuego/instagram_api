from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .location import Location

__all__ = ['LocationItem', 'LocationItemInterface']


class LocationItemInterface(ApiInterfaceBase):
    media_bundles: AnyType
    subtitle: AnyType
    location: Location
    title: AnyType


class LocationItem(PropertyMapper, LocationItemInterface):
    pass
