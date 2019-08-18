from typing import List

from instagram_api import response

from .base import CollectionBase

__all__ = ['Highlight']


class Highlight(CollectionBase):

    def get_user_feed(self, user_id: int) -> response.HighlightFeedResponse: ...

    def get_self_user_feed(self) -> response.HighlightFeedResponse: ...

    def create(self,
               media_ids: List[int],
               title: str = 'Highlights',
               cover_media_id: int = None,
               module: str = 'self_profile') -> response.CreateHighlightResponse: ...

    def edit(self,
             highlight_reel_id: str,
             params: dict,
             module: str = 'self_profile') -> response.HighlightFeedResponse: ...

    def delete(self, highlight_reel_id: str) -> response.GenericResponse: ...
