from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .story_tray import StoryTray

__all__ = ['TraySuggestions', 'TraySuggestionsInterface']


class TraySuggestionsInterface(ApiInterfaceBase):
    tray: [StoryTray]
    tray_title: str
    banner_title: str
    banner_subtitle: str
    suggestion_type: str


class TraySuggestions(PropertyMapper, TraySuggestionsInterface):
    pass
