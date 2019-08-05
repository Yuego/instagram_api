from instagram_api.property_mapper import PropertyMapperBase

from .generic_megaphone import GenericMegaphone

__all__ = ['Megaphone']


class Megaphone(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'generic_megaphone': GenericMegaphone,
    }
