from instagram_api.property_mapper import PropertyMapperBase

from .broadcast import Broadcast

__all__ = ['LiveVideoShare']


class LiveVideoShare(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
        'broadcast': Broadcast,
        'video_offset': int,
    }
