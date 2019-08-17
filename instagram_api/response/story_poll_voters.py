from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import VoterInfo

__all__ = ['StoryPollVotersResponse']


class StoryPollVotersResponseInterface(ApiResponseInterface):
    voter_info: VoterInfo


class StoryPollVotersResponse(ApiResponse, StoryPollVotersResponseInterface):
    pass
