from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .business_manager import BusinessManager
from .image import Image

__all__ = ['ShadowInstagramUser', 'ShadowInstagramUserInterface']


class ShadowInstagramUserInterface(ApiInterfaceBase):
    id: int
    instagram_user_id: int
    followers_count: int
    username: str
    profile_picture: Image
    business_manager: BusinessManager
    error: AnyType


class ShadowInstagramUser(PropertyMapper, ShadowInstagramUserInterface):
    pass
