from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['BiographyEntities']


class BiographyEntities(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'entities': None,
        'raw_text': str,
        'nux_type': str,
    }
