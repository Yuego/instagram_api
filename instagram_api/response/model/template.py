from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Template', 'TemplateInterface']


class TemplateInterface(ApiInterfaceBase):
    name: str
    parameters: AnyType


class Template(PropertyMapper, TemplateInterface):
    pass
