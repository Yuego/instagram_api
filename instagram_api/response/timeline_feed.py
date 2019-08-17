from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import FeedAysf, FeedItem

__all__ = ['TimelineFeedResponse']


class TimelineFeedResponseInterface(ApiResponseInterface):
    num_results: int
    client_gap_enforcer_matrix: AnyType
    is_direct_v2_enabled: bool
    auto_load_more_enabled: bool
    more_available: bool
    next_max_id: str
    pagination_info: AnyType
    feed_items: [FeedItem]
    megaphone: FeedAysf
    client_feed_changelist_applied: bool
    view_state_version: str
    feed_pill_text: str
    client_session_id: str


class TimelineFeedResponse(ApiResponse, TimelineFeedResponseInterface):
    pass
