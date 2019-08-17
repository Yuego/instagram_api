from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .user import User

__all__ = ['BroadcastQuestion', 'BroadcastQuestionInterface']


class BroadcastQuestionInterface(ApiInterfaceBase):
    text: str
    qid: str
    source: str
    user: User
    story_sticker_text: str
    timestamp: str


class BroadcastQuestion(PropertyMapper, BroadcastQuestionInterface):
    pass
