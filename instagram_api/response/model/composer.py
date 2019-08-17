from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Composer', 'ComposerInterface']


class ComposerInterface(ApiInterfaceBase):
    nux_finished: bool


class Composer(PropertyMapper, ComposerInterface):
    pass
