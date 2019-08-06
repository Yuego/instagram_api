from instagram_api.property_mapper import PropertyMapperBase

from .user import User

__all__ = ['TopLive']


class TopLive(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'broadcast_owners': [User],
        'ranked_position': None
    }
