from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Composer']


class Composer(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'nux_finished': bool,
    }
