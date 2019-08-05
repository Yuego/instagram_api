from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['QPSurface']


class QPSurface(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'surface_id': int,
        'cooldown': int,
    }
