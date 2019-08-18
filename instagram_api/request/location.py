from typing import List

from instagram_api import response
from instagram_api.response.model import Item
from .base import CollectionBase

__all__ = ['Location']


class Location(CollectionBase):

    def search(self, latitude: float, longitude: float, query: str = None) -> response.LocationResponse: ...

    def find_places(self,
                    query: str,
                    exclude_list: List[int] = None,
                    rank_token: str = None) -> response.FBLocationResponse: ...

    def find_places_nearby(self,
                           latitude: float,
                           longitude: float,
                           query: str = None,
                           exclude_list: List[int] = None,
                           rank_token: str = None) -> response.FBLocationResponse: ...

    def get_related(self, location_id: int) -> response.RelatedLocationResponse: ...

    def get_feed(self,
                 location_id: int,
                 rank_token: str,
                 tab: str = 'ranked',
                 next_media_ids: List[int] = None,
                 next_page: int = None,
                 max_id: str = None) -> response.LocationFeedResponse: ...

    def get_story_feed(self, location_id: int) -> response.LocationStoryResponse: ...

    def mark_story_media_seen(self,
                              location_feed: response.LocationStoryResponse,
                              items: List[Item]) -> response.MediaSeenResponse: ...
