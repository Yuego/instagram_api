from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['QPSurface', 'QPSurfaceInterface']


class QPSurfaceInterface(ApiInterfaceBase):
    surface_id: int
    cooldown: int


class QPSurface(PropertyMapper, QPSurfaceInterface):
    pass
