from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Challenge']


class Challenge(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'url': str,
        'api_path': None,
        'hide_webview_header': None,
        'lock': None,
        'logout': None,
        'native_flow': None,
    }
