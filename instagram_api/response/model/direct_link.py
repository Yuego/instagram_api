from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .link_context import LinkContext

__all__ = ['DirectLink', 'DirectLinkInterface']


class DirectLinkInterface(ApiInterfaceBase):
    text: str
    link_context: LinkContext


class DirectLink(PropertyMapper, DirectLinkInterface):
    pass
