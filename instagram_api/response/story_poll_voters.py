from .base_response import ApiResponse
from .model import VoterInfo

__all__ = ['StoryPollVotersResponse']


class StoryPollVotersResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'voter_info': VoterInfo,
    }
