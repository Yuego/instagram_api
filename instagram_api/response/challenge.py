from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['ChallengeResponse']


class ChallengeResponseInterface(ApiResponseInterface):
    pass


class ChallengeResponse(ApiResponse, ChallengeResponseInterface):
    pass
