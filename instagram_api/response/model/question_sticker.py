from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['QuestionSticker']


class QuestionSticker(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'question_id': int,
        'question': str,
        'text_color': str,
        'background_color': str,
        'viewer_can_interact': bool,
        'profile_pic_url': str,
        'question_type': str,
    }
