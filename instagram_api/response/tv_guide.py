from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Badging, Composer, TvChannel

__all__ = ['TvGuideResponse']


class TvGuideResponseInterface(ApiResponseInterface):
    channels: [TvChannel]
    my_channel: TvChannel
    badging: Badging
    composer: Composer


class TvGuideResponse(ApiResponse, TvGuideResponseInterface):
    pass
