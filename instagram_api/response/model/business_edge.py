from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .business_node import BusinessNode

__all__ = ['BusinessEdge', 'BusinessEdgeInterface']


class BusinessEdgeInterface(ApiInterfaceBase):
    node: BusinessNode
    cursor: AnyType


class BusinessEdge(PropertyMapper, BusinessEdgeInterface):
    pass
