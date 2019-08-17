from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .tv_channel import TvChannel
from .user import User

__all__ = ['TvSearchResult', 'TvSearchResultInterface']


class TvSearchResultInterface(ApiInterfaceBase):
    type: str
    User: User
    channel: TvChannel
    num_results: int
    rank_token: str


class TvSearchResult(PropertyMapper, TvSearchResultInterface):
    pass
