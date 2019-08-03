from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['DismissCard']


class DismissCard(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'card_id': int,
        'image_url': str,
        'title': None,
        'message': None,
        'button_text': None,
        'camera_target': None,
        'face_filter_id': None,
    }
