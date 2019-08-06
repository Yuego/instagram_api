from instagram_api.property_mapper import PropertyMapperBase

from .tv_channel import TVChannel
from .user import User

__all__ = ['TVSearchResult']


class TVSearchResult(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': str,
        'User': User,
        'channel': TVChannel,
        'num_results': int,
        'rank_token': str,
    }
