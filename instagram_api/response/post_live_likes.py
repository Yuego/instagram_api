from .base_response import Response

__all__ = ['PostLiveLikesResponse']


class PostLiveLikesResponse(Response):
    JSON_PROPERTY_MAP = {
        'starting_offset': None,
        'ending_offset': None,
        'next_fetch_offset': None,
        'time_series': None,
    }
