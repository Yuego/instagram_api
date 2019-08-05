from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['RewriteRule']


class RewriteRule(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'matcher': str,
        'replacer': str,
    }
