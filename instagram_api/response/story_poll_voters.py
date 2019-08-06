from .base_response import Response
from .model import VoterInfo

__all__ = ['StoryPollVotersResponse']


class StoryPollVotersResponse(Response):
    JSON_PROPERTY_MAP = {
        'voter_info': VoterInfo,
    }
