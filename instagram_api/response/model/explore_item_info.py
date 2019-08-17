from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['ExploreItemInfo', 'ExploreItemInfoInterface']


class ExploreItemInfoInterface(ApiInterfaceBase):
    num_columns: int
    total_num_columns: int
    aspect_ratio: int
    autoplay: bool
    destination_view: str


class ExploreItemInfo(PropertyMapper, ExploreItemInfoInterface):
    pass
