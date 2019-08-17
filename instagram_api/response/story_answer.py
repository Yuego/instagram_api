from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import StoryQuestionResponderInfos

__all__ = ['StoryAnswerResponse']


class StoryAnswerResponseInterface(ApiResponseInterface):
    responder_info: StoryQuestionResponderInfos


class StoryAnswerResponse(ApiResponse, StoryAnswerResponseInterface):
    pass
