from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['EndOfFeedDemarcator']


class EndOfFeedDemarcator(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'title': str,
        'subtitle': str,
    }
