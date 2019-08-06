from .base_response import Response
from .model import Item, Section, StoryTray

__all__ = ['TagFeedResponse']


class TagFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'sections': [Section],
        'num_results': int,
        'ranked_items': [Item],
        'auto_load_more_enabled': bool,
        'items': [Item],
        'story': StoryTray,
        'more_available': bool,
        'next_max_id': str,
        'next_media_ids': None,
        'next_page': int,
    }
