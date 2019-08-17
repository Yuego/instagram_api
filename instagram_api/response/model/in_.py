from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .product import Product
from .user import User

__all__ = ['In', 'InInterface']


class InInterface(ApiInterfaceBase):
    position: [float]
    user: User
    time_in_video: AnyType
    start_time_in_video_in_sec: AnyType
    duration_in_video_in_sec: AnyType
    product: Product


class In(PropertyMapper, InInterface):
    pass
