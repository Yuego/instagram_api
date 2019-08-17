from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .generic_megaphone import GenericMegaphone

__all__ = ['Megaphone', 'MegaphoneInterface']


class MegaphoneInterface(ApiInterfaceBase):
    generic_megaphone: GenericMegaphone


class Megaphone(PropertyMapper, MegaphoneInterface):
    pass
