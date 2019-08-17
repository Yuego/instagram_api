from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .viewer import Viewer

__all__ = ['QPViewerData', 'QPViewerDataInterface']


class QPViewerDataInterface(ApiInterfaceBase):
    viewer: Viewer


class QPViewerData(PropertyMapper, QPViewerDataInterface):
    pass
