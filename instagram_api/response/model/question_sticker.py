from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['QuestionSticker', 'QuestionStickerInterface']


class QuestionStickerInterface(ApiInterfaceBase):
    question_id: int
    question: str
    text_color: str
    background_color: str
    viewer_can_interact: bool
    profile_pic_url: str
    question_type: str


class QuestionSticker(PropertyMapper, QuestionStickerInterface):
    pass
