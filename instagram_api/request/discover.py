from typing import List, Optional

from .collection import Collection


class Discover(Collection):

    def get_explore_feed(self, max_id: str, is_prefetch: bool = False): ...

    def report_explore_media(self, explore_source_token: str, user_id: int): ...

    def search(self,
               query: str,
               latitude: float = None,
               longitude: float = None,
               exclude_list: List[int] = None,
               rank_token: Optional[str] = None): ...

    def get_suggested_searches(self, type: str): ...

    def get_recent_searches(self): ...

    def clean_search_history(self): ...
