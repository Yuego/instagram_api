from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .account_summary_unit import AccountSummaryUnit
from .business_feed import BusinessFeed
from .business_node import BusinessNode
from .promotions_unit import PromotionsUnit

__all__ = ['BusinessManager', 'BusinessManagerInterface']


class BusinessManagerInterface(ApiInterfaceBase):
    account_summary_unit: AccountSummaryUnit
    account_insights_unit: BusinessNode
    followers_unit: BusinessNode
    top_posts_unit: BusinessNode
    stories_unit: BusinessNode
    promotions_unit: PromotionsUnit
    feed: BusinessFeed


class BusinessManager(PropertyMapper, BusinessManagerInterface):
    pass
