from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType, Lazy


__all__ = ['Channel', 'ChannelInterface']


class ChannelInterface(ApiInterfaceBase):
    channel_id: int
    channel_type: AnyType
    title: AnyType
    header: AnyType
    media_count: int
    media: Lazy.model__item__Item
    context: AnyType


class Channel(PropertyMapper, ChannelInterface):
    pass
