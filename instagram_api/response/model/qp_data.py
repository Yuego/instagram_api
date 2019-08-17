from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .qp_viewer_data import QPViewerData

__all__ = ['QPData', 'QPDataInterface']


class QPDataInterface(ApiInterfaceBase):
    surface: int
    data: QPViewerData


class QPData(PropertyMapper, QPDataInterface):
    pass
