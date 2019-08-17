from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AndroidLinks', 'AndroidLinksInterface']


class AndroidLinksInterface(ApiInterfaceBase):
    linkType: int
    webUri: str
    androidClass: str
    package: str
    deeplinkUri: str
    callToActionTitle: str
    redirectUri: str
    igUserId: str
    leadGenFormId: str
    canvasDocId: str


class AndroidLinks(PropertyMapper, AndroidLinksInterface):
    pass
