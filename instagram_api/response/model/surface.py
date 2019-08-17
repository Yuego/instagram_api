from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Surface', 'SurfaceInterface']


class SurfaceInterface(ApiInterfaceBase):
    scores: AnyType
    rank_token: str
    ttl_secs: int
    name: str


class Surface(PropertyMapper, SurfaceInterface):
    pass
