
from .base import PropertyMapperBase

__all__ = ['PropertyMapperErrorList']


class PropertyMapperErrorList(PropertyMapperBase):

    JSON_PROPERTY_MAP = {
        'errors': [str],
    }
