from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .suggestion import Suggestion

__all__ = ['FeedAysf', 'FeedAysfInterface']


class FeedAysfInterface(ApiInterfaceBase):
    landing_site_type: AnyType
    uuid: str
    view_all_text: AnyType
    feed_position: AnyType
    landing_site_title: AnyType
    is_dismissable: AnyType
    suggestions: [Suggestion]
    should_refill: AnyType
    display_new_unit: AnyType
    fetch_user_details: AnyType
    title: AnyType
    activator: AnyType


class FeedAysf(PropertyMapper, FeedAysfInterface):
    pass
