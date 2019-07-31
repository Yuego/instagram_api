from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AdMetadata']


class AdMetadata(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'value': None,
        'type': None,
    }
