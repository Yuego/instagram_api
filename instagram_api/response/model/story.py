from instagram_api.property_mapper import PropertyMapperBase

from .args import Args
from .counts import Counts

__all__ = ['Story']


class Story(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'pk': int,
        'counts': Counts,
        'args': Args,
        'type': int,
        'story_type': int,
    }
