from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['HiddenEntities']


class HiddenEntities(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'user': None,
        'hashtag': None,
        'place': None,
    }
