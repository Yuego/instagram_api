from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['BroadcastHeartbeatAndViewerCountResponse']


class BroadcastHeartbeatAndViewerCountResponseInterface(ApiResponseInterface):
    broadcast_status: str
    viewer_count: int
    offset_to_video_start: int
    total_unique_viewer_count: int
    is_top_live_eligible: int
    cobroadcaster_ids: [str]
    is_policy_violation: int
    policy_violation_reason: str


class BroadcastHeartbeatAndViewerCountResponse(ApiResponse, BroadcastHeartbeatAndViewerCountResponseInterface):
    pass
