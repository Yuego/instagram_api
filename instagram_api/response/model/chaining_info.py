from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['ChainingInfo', 'ChainingInfoInterface']


class ChainingInfoInterface(ApiInterfaceBase):
    sources: str


class ChainingInfo(PropertyMapper, ChainingInfoInterface):
    pass
