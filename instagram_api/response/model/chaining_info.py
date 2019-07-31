from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['ChainingInfo']


class ChainingInfo(PropertyMapperBase):

    JSON_PROPERTY_MAP = {
        'sources': str,
    }
