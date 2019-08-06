from instagram_api.property_mapper import PropertyMapperBase

from .tv_channel import TvChannel
from .user import User

__all__ = ['TvSearchResult']


class TvSearchResult(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'type': str,
        'User': User,
        'channel': TvChannel,
        'num_results': int,
        'rank_token': str,
    }
