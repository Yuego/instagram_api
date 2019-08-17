from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['EndOfFeedDemarcator', 'EndOfFeedDemarcatorInterface']


class EndOfFeedDemarcatorInterface(ApiInterfaceBase):
    id: int
    title: str
    subtitle: str


class EndOfFeedDemarcator(PropertyMapper, EndOfFeedDemarcatorInterface):
    pass
