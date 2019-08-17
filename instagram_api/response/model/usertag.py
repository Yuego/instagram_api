from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .in_ import In

__all__ = ['Usertag', 'UsertagInterface']


# TODO: разобраться со служебными словами
class UsertagInterface(ApiInterfaceBase):
    in__: [In]
    photo_of_you: bool


class Usertag(PropertyMapper, UsertagInterface):
    pass
