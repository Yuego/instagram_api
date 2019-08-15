from .base_response import ApiResponse
from .model import BlockedReels

__all__ = ['BlockedReelsResponse']


class BlockedReelsResponse(ApiResponse, BlockedReels):
    JSON_PROPERTY_MAP = {
        'next_max_id': str,
    }
