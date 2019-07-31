from instagram_api.property_mapper import PropertyMapperBase

from .link_context import LinkContext

__all__ = ['Link']


class Link(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'start': int,
        'end': int,
        'id': str,
        'type': str,
        'text': str,
        'link_context': LinkContext,
    }
