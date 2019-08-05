from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['PrimaryCountryInfo']


class PrimaryCountryInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'is_visible': bool,
        'has_country': bool,
        'country_name': str,
    }
