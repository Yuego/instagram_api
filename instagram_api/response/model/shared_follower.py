from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['SharedFollower', 'SharedFollowerInterface']


class SharedFollowerInterface(ApiInterfaceBase):
    pk: int
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: str
    profile_pic_id: int
    is_verified: bool
    has_anonymous_profile_picture: bool
    reel_auto_archive: str
    overlap_score: str


class SharedFollower(PropertyMapper, SharedFollowerInterface):
    pass
