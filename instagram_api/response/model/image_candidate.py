from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['ImageCandidate']


class ImageCandidate(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'url': str,
        'width': int,
        'height': int,
        'estimated_scans_sizes': [int],
    }
