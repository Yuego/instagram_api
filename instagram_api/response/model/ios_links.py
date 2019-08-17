from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['IOSLinks', 'IOSLinksInterface']


class IOSLinksInterface(ApiInterfaceBase):
    linkType: int
    canvasDocId: str


class IOSLinks(PropertyMapper, IOSLinksInterface):
    pass
