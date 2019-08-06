from .base_response import Response

__all__ = ['BroadcastHeartbeatAndViewerCountResponse']


class BroadcastHeartbeatAndViewerCountResponse(Response):
    JSON_PROPERTY_MAP = {
        'broadcast_status': str,
        'viewer_count': int,
        'offset_to_video_start': int,
        'total_unique_viewer_count': int,
        'is_top_live_eligible': int,
        'cobroadcaster_ids': [str],
        'is_policy_violation': int,
        'policy_violation_reason': str,
    }
