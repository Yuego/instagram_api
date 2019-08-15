from .base_response import ApiResponse
from .model import BroadcastQuestion

__all__ = ['BroadcastQuestionsResponse']


class BroadcastQuestionsResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'questions': [BroadcastQuestion],
    }
