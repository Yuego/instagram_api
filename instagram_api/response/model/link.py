from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .link_context import LinkContext

__all__ = ['Link', 'LinkInterface']


class LinkInterface(ApiInterfaceBase):
    start: int
    end: int
    id: str
    type: str
    text: str
    link_context: LinkContext


class Link(PropertyMapper, LinkInterface):
    pass
