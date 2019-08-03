from instagram_api.property_mapper import PropertyMapperBase

from .suggestion import Suggestion

__all__ = ['FeedAysf']


class FeedAysf(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'landing_site_type': None,
        'uuid': 'string',
        'view_all_text': None,
        'feed_position': None,
        'landing_site_title': None,
        'is_dismissable': None,
        'suggestions': [Suggestion],
        'should_refill': None,
        'display_new_unit': None,
        'fetch_user_details': None,
        'title': None,
        'activator': None,
    }
