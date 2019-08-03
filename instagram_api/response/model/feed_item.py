from instagram_api.property_mapper import PropertyMapperBase

from .ad_4_ad import Ad4ad
from .end_of_feed_demarcator import EndOfFeedDemarcator
from .item import Item
from .stories_netego import StoriesNetego
from .suggested_users import SuggestedUsers

__all__ = ['FeedItem']


class FeedItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'media_or_ad': Item,
        'stories_netego': StoriesNetego,
        'ad4ad': Ad4ad,
        'suggested_users': SuggestedUsers,
        'end_of_feed_demarcator': EndOfFeedDemarcator,
        'ad_link_type': int,
    }
