from typing import List, Optional

from instagram_api import response

from .base import CollectionBase

__all__ = ['Discover']


class Discover(CollectionBase):

    def get_explore_feed(self, max_id: str = None, is_prefetch: bool = False) -> response.ExploreResponse: ...

    def report_explore_media(self, explore_source_token: str, user_id: int) -> response.ReportExploreMediaResponse: ...

    def search(self,
               query: str,
               latitude: float = None,
               longitude: float = None,
               exclude_list: List[int] = None,
               rank_token: Optional[str] = None) -> response.FBSearchResponse: ...

    def get_suggested_searches(self, type: str) -> response.SuggestedSearchesResponse: ...

    def get_recent_searches(self) -> response.RecentSearchesResponse: ...

    def clear_search_history(self) -> response.GenericResponse: ...
