from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Item, Section, StoryTray

__all__ = ['TagFeedResponse']


class TagFeedResponseInterface(ApiResponseInterface):
    sections: [Section]
    num_results: int
    ranked_items: [Item]
    auto_load_more_enabled: bool
    items: [Item]
    story: StoryTray
    more_available: bool
    next_max_id: str
    next_media_ids: AnyType
    next_page: int


class TagFeedResponse(ApiResponse, TagFeedResponseInterface):
    pass
