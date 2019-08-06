from .base_response import Response

__all__ = ['PresencesResponse']


class PresencesResponse(Response):
    JSON_PROPERTY_MAP = {
        'user_presence': 'Model\UnpredictableKeys\PresenceUnpredictableContainer',
    }
