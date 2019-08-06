from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['CountdownSticker']


class CountdownSticker(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'countdown_id': int,
        'end_ts': str,
        'text': str,
        'text_color': str,
        'start_background_color': str,
        'end_background_color': str,
        'digit_color': str,
        'digit_card_color': str,
        'following_enabled': bool,
        'is_owner': bool,
        'attribution': None,
        'viewer_is_following': bool,
    }
