from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Insights']


class Insights(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'instagram_insights': None,
    }
