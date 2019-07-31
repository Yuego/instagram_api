from instagram_api.property_mapper import PropertyMapperBase

from .bold import Bold

__all__ = ['ActionLog']


class ActionLog(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'bold': [Bold],
        'description': str,
    }
