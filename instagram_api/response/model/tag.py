from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Tag', 'TagInterface']


class TagInterface(ApiInterfaceBase):
    id: int
    name: str
    media_count: int
    type: str
    follow_status: AnyType
    following: AnyType
    allow_following: AnyType
    allow_muting_story: AnyType
    profile_pic_url: AnyType
    non_violating: AnyType
    related_tags: AnyType
    subtitle: AnyType
    social_context: AnyType
    social_context_profile_links: AnyType
    show_follow_drop_down: AnyType
    follow_button_text: AnyType
    debug_info: AnyType
    search_result_subtitle: AnyType


class Tag(PropertyMapper, TagInterface):
    pass
