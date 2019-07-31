from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['FriendshipStatus']


class FriendshipStatus(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'following': bool,
        'followed_by': bool,
        'incoming_request': bool,
        'outgoing_request': bool,
        'is_private': bool,
        'is_blocking_reel': bool,
        'is_muting_reel': bool,
        'blocking': bool,
        'muting': bool,
        'is_bestie': bool,
        'is_restricted': bool,
    }
