from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['LinkContext']


class LinkContext(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'link_url': str,
        'link_title': str,
        'link_summary': str,
        'link_image_url': str,
    }
