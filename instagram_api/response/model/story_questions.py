from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .question_sticker import QuestionSticker

__all__ = ['StoryQuestions', 'StoryQuestionsInterface']


class StoryQuestionsInterface(ApiInterfaceBase):
    x: float
    y: float
    z: float
    width: float
    height: float
    rotation: float
    is_pinned: int
    is_hidden: int
    question_sticker: QuestionSticker


class StoryQuestions(PropertyMapper, StoryQuestionsInterface):
    pass
