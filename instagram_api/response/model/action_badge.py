from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['ActionBadge', 'ActionBadgeInterface']


class ActionBadgeInterface(ApiInterfaceBase):
    action_type: AnyType
    action_count: int
    action_timestamp: Timestamp


class ActionBadge(PropertyMapper, ActionBadgeInterface):
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
