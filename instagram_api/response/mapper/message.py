from .interface_base import ApiInterfaceBase
from .mapper_base import PropertyMapperBase
from .mapper_meta import PropertyMapperMeta
from .types import AnyType

class MessageInterface(ApiInterfaceBase):
    key: AnyType
    time: AnyType


class Message(PropertyMapperBase, MessageInterface, metaclass=PropertyMapperMeta):
    pass
