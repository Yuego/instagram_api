from .base_response import Response

__all__ = ['BadgeNotificationsResponse']


class BadgeNotificationsResponse(Response):
    JSON_PROPERTY_MAP = {
        'badge_payload': 'Model\UnpredictableKeys\CoreUnpredictableContainer',
    }
