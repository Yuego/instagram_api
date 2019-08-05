from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Slot']


class Slot(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'slot': int,
        'cooldown': int,
    }
