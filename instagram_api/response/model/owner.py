from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .location import Location

__all__ = ['Owner', 'OwnerInterface']


class OwnerInterface(ApiInterfaceBase):
    type: AnyType
    pk: int
    name: str
    profile_pic_url: str
    profile_pic_username: str
    short_name: str
    lat: float
    lng: float
    location_dict: Location


class Owner(PropertyMapper, OwnerInterface):
    pass
