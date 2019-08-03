from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Effect']


class Effect(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'title': str,
        'id': int,
        'effect_id': int,
        'effect_file_id': int,
        'asset_url': str,
        'thumbnail_url': str,
        'instructions': None,
    }
