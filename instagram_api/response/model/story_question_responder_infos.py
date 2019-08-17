from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .responder import Responder

__all__ = ['StoryQuestionResponderInfos', 'StoryQuestionResponderInfosInterface']


class StoryQuestionResponderInfosInterface(ApiInterfaceBase):
    question_id: int
    question: str
    question_type: str
    background_color: str
    text_color: str
    responders: [Responder]
    max_id: int
    more_available: bool
    question_response_count: int
    latest_question_response_time: int


class StoryQuestionResponderInfos(PropertyMapper, StoryQuestionResponderInfosInterface):
    pass
