from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['PageInfo']


class PageInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'end_cursor': str,
        'has_next_page': bool,
        'has_previous_page': bool,
    }
