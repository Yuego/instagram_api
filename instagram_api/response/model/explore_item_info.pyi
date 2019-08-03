from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['ExploreItemInfo']


class ExploreItemInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'num_columns': int,
        'total_num_columns': int,
        'aspect_ratio': int,
        'autoplay': bool,
        'destination_view': str,
    }
