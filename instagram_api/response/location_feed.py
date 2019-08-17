from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Section

__all__ = ['LocationFeedResponse']


class LocationFeedResponseInterface(ApiResponseInterface):
    sections: [Section]
    next_page: int
    more_available: bool
    next_media_ids: [int]
    next_max_id: str


class LocationFeedResponse(ApiResponse, LocationFeedResponseInterface):
    pass
