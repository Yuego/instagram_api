from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['SystemControl', 'SystemControlInterface']


class SystemControlInterface(ApiInterfaceBase):
    upload_max_bytes: int
    upload_time_period_sec: int
    upload_bytes_per_update: int


class SystemControl(PropertyMapper, SystemControlInterface):
    pass
