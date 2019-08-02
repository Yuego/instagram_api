from instagram_api.property_mapper import PropertyMapperBase

from .link_context import LinkContext

__all__ = ['DirectLink']


class DirectLink(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'text': str,
        'link_context': LinkContext,
    }
