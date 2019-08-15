from .base_response import ApiResponse

__all__ = ['PresenceStatusResponse']


class PresenceStatusResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'disabled': bool,
        'thread_presence_disabled': bool,
    }
