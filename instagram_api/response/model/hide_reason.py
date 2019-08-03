from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['HideReason']


class HideReason(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
        'reason': str,
    }
