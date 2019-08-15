from .base_response import ApiResponse
from .model import StoryQuestionResponderInfos

__all__ = ['StoryAnswerResponse']


class StoryAnswerResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'responder_info': StoryQuestionResponderInfos,
    }
