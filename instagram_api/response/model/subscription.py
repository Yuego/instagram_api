from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Subscription', 'SubscriptionInterface']


class SubscriptionInterface(ApiInterfaceBase):
    topic: AnyType
    url: str
    sequence: AnyType
    auth: AnyType


class Subscription(PropertyMapper, SubscriptionInterface):
    pass
