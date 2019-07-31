from instagram_api.property_mapper import PropertyMapperBase

from .account_summary_unit import AccountSummaryUnit
from .business_feed import BusinessFeed
from .business_node import BusinessNode
from .promotions_unit import PromotionsUnit

__all__ = ['BusinessManager']


class BusinessManager(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'account_summary_unit': AccountSummaryUnit,
        'account_insights_unit': BusinessNode,
        'followers_unit': BusinessNode,
        'top_posts_unit': BusinessNode,
        'stories_unit': BusinessNode,
        'promotions_unit': PromotionsUnit,
        'feed': BusinessFeed,
    }
