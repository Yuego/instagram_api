from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['VideoCallEvent', 'VideoCallEventInterface']


class VideoCallEventInterface(ApiInterfaceBase):
    action: str
    vc_id: str


class VideoCallEvent(PropertyMapper, VideoCallEventInterface):
    VIDEO_CALL_STARTED = 'video_call_started'
    VIDEO_CALL_JOINED = 'video_call_joined'
    VIDEO_CALL_LEFT = 'video_call_left'
    VIDEO_CALL_ENDED = 'video_call_ended'
    UNKNOWN = 'unknown'
