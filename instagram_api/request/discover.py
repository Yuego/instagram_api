from typing import List, Optional

import json
import time

from instagram_api import response
from instagram_api.constants import Constants

from .base import CollectionBase

__all__ = ['Discover']


class Discover(CollectionBase):

    def get_explore_feed(self, max_id: str = None, is_prefetch: bool = False) -> response.ExploreResponse:
        request = self._ig.request('discover/explore/').add_params(**{
            'is_prefetch': is_prefetch,
            'is_from_promote': False,
            'timezone_offset': time.timezone,
            'session_id': self._ig.session_id,
            'supported_capabilities_new': json.dumps(Constants.SUPPORTED_CAPABILITIES),
        })

        if not is_prefetch:
            if max_id is None:
                max_id = 0

            request.add_params(**{
                'max_id': max_id,
                'module': 'explore_popular',
            })

        return request.get_response(response.ExploreResponse)

    def report_explore_media(self, explore_source_token: str, user_id: int) -> response.ReportExploreMediaResponse: ...

    def search(self,
               query: str,
               latitude: float = None,
               longitude: float = None,
               exclude_list: List[int] = None,
               rank_token: Optional[str] = None) -> response.FBSearchResponse: ...

    def get_suggested_searches(self, search_type: str) -> response.SuggestedSearchesResponse:
        assert search_type in ['blended', 'users', 'hashtags', 'places'], f'Unknown search type: {search_type}'

        return self._ig.request('fbsearch/suggested_searches/').add_params(**{
            'type': search_type,
        }).get_response(response.SuggestedSearchesResponse)

    def get_recent_searches(self) -> response.RecentSearchesResponse:
        return self._ig.request('fbsearch/recent_searches/').get_response(response.RecentSearchesResponse)

    def clear_search_history(self) -> response.GenericResponse: ...
