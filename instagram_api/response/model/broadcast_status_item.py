from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['BroadcastStatusitem']


class BroadcastStatusitem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'broadcast_status': str,
        'has_reduced_visibility': bool,
        'cover_frame_url': str,
        'viewer_count': int,
        'id': int,
    }
