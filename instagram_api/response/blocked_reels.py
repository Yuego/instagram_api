from .mapper import ApiResponse

from .model.blocked_reels import BlockedReelsInterface

__all__ = ['BlockedReelsResponse']


class BlockedReelsResponseInterface(BlockedReelsInterface):
    next_max_id: str


class BlockedReelsResponse(ApiResponse, BlockedReelsResponseInterface):
    pass
