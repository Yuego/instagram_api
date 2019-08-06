from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

from .user import User

__all__ = ['Broadcast']


class Broadcast(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'broadcast_owner': User,
        'broadcast_status': str,
        'cover_frame_url': str,
        'published_time': str,
        'broadcast_message': str,
        'muted': None,
        'media_id': int,
        'id': str,
        'rtmp_playback_url': str,
        'dash_abr_playback_url': str,
        'dash_playback_url': str,
        'ranked_position': None,
        'organic_tracking_token': str,
        'seen_ranked_position': None,
        'viewer_count': int,
        'dash_manifest': str,

        'expire_at': timestamp,
        'encoding_tag': str,
        'total_unique_viewer_count': int,
        'internal_only': bool,
        'number_of_qualities': int,
    }
