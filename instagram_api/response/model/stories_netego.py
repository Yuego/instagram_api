from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['StoriesNetego']


class StoriesNetego(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'tracking_token': str,
        'hide_unit_if_seen': str,
        'id': int,
    }
