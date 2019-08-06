from .base_response import Response
from .model import FormerUsername

__all__ = ['FormerUsernamesResponse']


class FormerUsernamesResponse(Response):
    JSON_PROPERTY_MAP = {
        'former_usernames': [FormerUsername],
    }
