from .base_response import Response
from .model import BroadcastQuestion

__all__ = ['BroadcastQuestionsResponse']


class BroadcastQuestionsResponse(Response):
    JSON_PROPERTY_MAP = {
        'questions': [BroadcastQuestion],
    }
