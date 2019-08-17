from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .qp_node import QPNode
from .time_range import TimeRange

__all__ = ['Edges', 'EdgesInterface']


class EdgesInterface(ApiInterfaceBase):
    priority: int
    time_range: TimeRange
    node: QPNode


class Edges(PropertyMapper, EdgesInterface):
    pass
