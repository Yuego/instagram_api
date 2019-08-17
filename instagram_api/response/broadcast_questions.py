from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import BroadcastQuestion

__all__ = ['BroadcastQuestionsResponse']


class BroadcastQuestionsResponseInterface(ApiResponseInterface):
    questions: [BroadcastQuestion]


class BroadcastQuestionsResponse(ApiResponse, BroadcastQuestionsResponseInterface):
    pass
