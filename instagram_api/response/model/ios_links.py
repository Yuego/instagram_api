from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['IOSLinks']


class IOSLinks(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'linkType': int,
        'canvasDocId': str,
    }
