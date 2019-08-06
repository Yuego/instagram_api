from .base_response import Response
from .model import FeedAysf, FeedItem

__all__ = ['TimelineFeedResponse']


class TimelineFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'num_results': int,
        'client_gap_enforcer_matrix': None,
        'is_direct_v2_enabled': bool,
        'auto_load_more_enabled': bool,
        'more_available': bool,
        'next_max_id': str,
        'pagination_info': None,
        'feed_items': [FeedItem],
        'megaphone': FeedAysf,
        'client_feed_changelist_applied': bool,
        'view_state_version': str,
        'feed_pill_text': str,
        'client_session_id': str,
    }
