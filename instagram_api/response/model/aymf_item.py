from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AymfItem']


class AymfItem(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'caption': str,
        'uuid': str,
    }
