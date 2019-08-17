from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['LinkContext', 'LinkContextInterface']


class LinkContextInterface(ApiInterfaceBase):
    link_url: str
    link_title: str
    link_summary: str
    link_image_url: str


class LinkContext(PropertyMapper, LinkContextInterface):
    pass
