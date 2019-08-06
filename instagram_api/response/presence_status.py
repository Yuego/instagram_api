from .base_response import Response

__all__ = ['PresenceStatusResponse']


class PresenceStatusResponse(Response):
    JSON_PROPERTY_MAP = {
        'disabled': bool,
        'thread_presence_disabled': bool,
    }
