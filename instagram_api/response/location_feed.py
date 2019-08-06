from .base_response import Response
from .model import Section

__all__ = ['LocationFeedResponse']


class LocationFeedResponse(Response):
    JSON_PROPERTY_MAP = {
        'sections': [Section],
        'next_page': int,
        'more_available': bool,
        'next_media_ids': [int],
        'next_max_id': str,
    }
