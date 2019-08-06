from instagram_api.property_mapper import PropertyMapperBase

from .voter import Voter

__all__ = ['VoterInfo']


class VoterInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'poll_id': int,
        'voters': [Voter],
        'max_id': int,
        'more_available': bool,
    }
