from instagram_api.property_mapper import PropertyMapperBase

from .question_sticker import QuestionSticker

__all__ = ['StoryQuestions']


class StoryQuestions(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'x': float,
        'y': float,
        'z': float,
        'width': float,
        'height': float,
        'rotation': float,
        'is_pinned': int,
        'is_hidden': int,
        'question_sticker': QuestionSticker,
    }
