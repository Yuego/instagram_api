from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['Broadcast', 'BroadcastInterface']


class BroadcastInterface(ApiInterfaceBase):
    broadcast_owner: User
    broadcast_status: str
    cover_frame_url: str
    published_time: str
    broadcast_message: str
    muted: AnyType
    media_id: int
    id: str
    rtmp_playback_url: str
    dash_abr_playback_url: str
    dash_playback_url: str
    ranked_position: AnyType
    organic_tracking_token: str
    seen_ranked_position: AnyType
    viewer_count: int
    dash_manifest: str

    expire_at: Timestamp
    encoding_tag: str
    total_unique_viewer_count: int
    internal_only: bool
    number_of_qualities: int


class Broadcast(PropertyMapper, BroadcastInterface):
    pass
