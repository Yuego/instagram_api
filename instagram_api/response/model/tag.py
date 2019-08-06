from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['Tag']


class Tag(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'name': str,
        'media_count': int,
        'type': str,
        'follow_status': None,
        'following': None,
        'allow_following': None,
        'allow_muting_story': None,
        'profile_pic_url': None,
        'non_violating': None,
        'related_tags': None,
        'subtitle': None,
        'social_context': None,
        'social_context_profile_links': None,
        'show_follow_drop_down': None,
        'follow_button_text': None,
        'debug_info': None,
        'search_result_subtitle': None,
    }
