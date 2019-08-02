from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Counts']


class Counts(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'relationships': None,
        'requests': None,
        'photos_of_you': None,
        'usertags': None,
        'comments': None,
        'likes': None,
        'comment_likes': None,
        'campaign_notification': None,
    }
