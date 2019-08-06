from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['VideoCallEvent']


class VideoCallEvent(PropertyMapperBase):
    VIDEO_CALL_STARTED = 'video_call_started'
    VIDEO_CALL_JOINED = 'video_call_joined'
    VIDEO_CALL_LEFT = 'video_call_left'
    VIDEO_CALL_ENDED = 'video_call_ended'
    UNKNOWN = 'unknown'

    JSON_PROPERTY_MAP = {
        'action': str,
        'vc_id': str,
    }
