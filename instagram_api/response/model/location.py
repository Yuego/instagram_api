from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType, Lazy

__all__ = ['Location', 'LocationInterface']


class LocationInterface(ApiInterfaceBase):
    name: str
    external_id_source: str
    external_source: str
    address: str
    lat: float
    lng: float
    external_id: int
    facebook_places_id: int
    city: str
    pk: str
    short_name: str
    facebook_events_id: int
    start_time: AnyType
    end_time: AnyType
    location_dict: Lazy.model__location__Location
    type: AnyType
    profile_pic_url: str
    profile_pic_username: str
    time_granularity: AnyType
    timezone: AnyType
    country: int
    created_at: int
    event_category: int
    place_fbid: str
    place_name: str


class Location(PropertyMapper, LocationInterface):
    pass
