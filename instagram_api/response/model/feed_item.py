from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .ad_4_ad import Ad4ad
from .end_of_feed_demarcator import EndOfFeedDemarcator
from .item import Item
from .stories_netego import StoriesNetego
from .suggested_users import SuggestedUsers

__all__ = ['FeedItem', 'FeedItemInterface']


class FeedItemInterface(ApiInterfaceBase):
    media_or_ad: Item
    stories_netego: StoriesNetego
    ad4ad: Ad4ad
    suggested_users: SuggestedUsers
    end_of_feed_demarcator: EndOfFeedDemarcator
    ad_link_type: int


class FeedItem(PropertyMapper, FeedItemInterface):
    pass
