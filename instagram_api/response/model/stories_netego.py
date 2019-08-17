from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['StoriesNetego', 'StoriesNetegoInterface']


class StoriesNetegoInterface(ApiInterfaceBase):
    tracking_token: str
    hide_unit_if_seen: str
    id: int


class StoriesNetego(PropertyMapper, StoriesNetegoInterface):
    pass
