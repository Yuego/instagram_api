from instagram_api.property_mapper import PropertyMapperBase

from .comment import Comment

__all__ = ['PropertyMapperBase']


class LiveComment(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'comment': Comment,
        'offset': None,
        'event': None,
    }
