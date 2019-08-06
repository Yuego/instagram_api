from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['UserPresence']


class UserPresence(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'user_id': int,
        'last_activity_at_ms': str,
        'is_active': bool,
        'in_threads': [str],
    }
