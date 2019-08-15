from .base_response import ApiResponse
from .model import Badging, Composer, TvChannel

__all__ = ['TvGuideResponse']


class TvGuideResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'channels': [TvChannel],
        'my_channel': TvChannel,
        'badging': Badging,
        'composer': Composer,
    }
