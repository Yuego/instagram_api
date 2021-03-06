from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .inline_follow import InlineFollow
from .link import Link
from .media import Media

__all__ = ['Args', 'ArgsInterface']


class ArgsInterface(ApiInterfaceBase):
    media_destination: str
    text: str
    icon_url: str
    links: [Link]
    rich_text: str
    profile_id: int
    profile_image: str
    media: [Media]
    comment_notif_type: str
    timestamp: str
    tuuid: str
    clicked: bool
    profile_name: str
    action_url: str
    destination: str
    actions: [str]
    latest_reel_media: str
    comment_id: int
    request_count: AnyType
    inline_follow: InlineFollow
    comment_ids: [int]
    second_profile_id: int
    second_profile_image: AnyType
    profile_image_destination: AnyType


class Args(PropertyMapper, ArgsInterface):
    pass
