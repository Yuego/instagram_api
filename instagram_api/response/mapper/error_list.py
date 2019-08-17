from .interface_base import ApiInterfaceBase
from .mapper_base import PropertyMapperBase
from .mapper_meta import PropertyMapperMeta

__all__ = ['ErrorList']


class ErrorListInterface(ApiInterfaceBase):
    errors: [str]


class ErrorList(PropertyMapperBase, ErrorListInterface, metaclass=PropertyMapperMeta):
    pass
