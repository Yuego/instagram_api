from instagram_api.property_mapper import PropertyMapperBase
from instagram_api.property_mapper.types import timestamp

__all__ = ['ActionBadge']


class ActionBadge(PropertyMapperBase):
    DELIVERED = 'raven_delivered'
    SENT = 'raven_sent'
    OPENED = 'raven_opened'
    SCREENSHOT = 'raven_screenshot'
    REPLAYED = 'raven_replayed'
    CANNOT_DELIVER = 'raven_cannot_deliver'
    SENDING = 'raven_sending'
    BLOCKED = 'raven_blocked'
    UNKNOWN = 'raven_unknown'
    SUGGESTED = 'raven_suggested'

    JSON_PROPERTY_MAP = {
        'action_type': None,
        'action_count': int,
        'action_timestamp': timestamp,
    }
