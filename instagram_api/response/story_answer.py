from .base_response import Response
from .model import StoryQuestionResponderInfos

__all__ = ['StoryAnswerResponse']


class StoryAnswerResponse(Response):
    JSON_PROPERTY_MAP = {
        'responder_info': StoryQuestionResponderInfos,
    }
