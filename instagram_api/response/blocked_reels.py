from .base_response import Response
from .model import BlockedReels

__all__ = ['BlockedReelsResponse']


class BlockedReelsResponse(Response, BlockedReels):
    JSON_PROPERTY_MAP = {
        'next_max_id': str,
    }
