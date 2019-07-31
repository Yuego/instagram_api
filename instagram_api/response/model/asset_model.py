from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AssetModel']


class AssetModel(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'asset_url': str,
        'id': int,
    }
