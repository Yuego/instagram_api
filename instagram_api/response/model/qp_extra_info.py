from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['QPExtraInfo', 'QPExtraInfoInterface']


class QPExtraInfoInterface(ApiInterfaceBase):
    surface: int
    extra_info: str


class QPExtraInfo(PropertyMapper, QPExtraInfoInterface):
    pass
