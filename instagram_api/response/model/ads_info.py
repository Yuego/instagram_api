from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AdsInfo']


class AdsInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'has_ads': bool,
        'ads_url': str,
    }
