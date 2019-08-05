from instagram_api.property_mapper import PropertyMapperBase

from .post_live_item import PostLiveItem

__all__ = ['PostLive']


class PostLive(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'post_live_items': [PostLiveItem],
    }
