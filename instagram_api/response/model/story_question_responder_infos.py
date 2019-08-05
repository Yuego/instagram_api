from instagram_api.property_mapper import PropertyMapperBase

from .responder import Responder

__all__ = ['StoryQuestionResponderInfos']


class StoryQuestionResponderInfos(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'question_id': int,
        'question': str,
        'question_type': str,
        'background_color': str,
        'text_color': str,
        'responders': [Responder],
        'max_id': int,
        'more_available': bool,
        'question_response_count': int,
        'latest_question_response_time': int,
    }
