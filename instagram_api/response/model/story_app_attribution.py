from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['StoryAppAttribution']


class StoryAppAttribution(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'app_action_text': str,
        'app_icon_url': str,
        'content_url': str,
        'id': int,
        'link': str,
        'name': str,
    }
