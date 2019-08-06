from .base_response import Response
from .model import Badging, Composer, TvChannel

__all__ = ['TvGuideResponse']


class TvGuideResponse(Response):
    JSON_PROPERTY_MAP = {
        'channels': [TvChannel],
        'my_channel': TvChannel,
        'badging': Badging,
        'composer': Composer,
    }
