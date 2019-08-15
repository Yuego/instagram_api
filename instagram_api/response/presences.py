from .base_response import ApiResponse

__all__ = ['PresencesResponse']


class PresencesResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'user_presence': 'Model\UnpredictableKeys\PresenceUnpredictableContainer',
    }
