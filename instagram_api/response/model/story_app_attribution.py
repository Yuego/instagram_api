from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['StoryAppAttribution', 'StoryAppAttributionInterface']


class StoryAppAttributionInterface(ApiInterfaceBase):
    app_action_text: str
    app_icon_url: str
    content_url: str
    id: int
    link: str
    name: str


class StoryAppAttribution(PropertyMapper, StoryAppAttributionInterface):
    pass
