from typing import List

from instagram_api import response
from instagram_api.response.model import Item

from .base import CollectionBase

__all__ = ['Hashtag']


class Hashtag(CollectionBase):

    def get_info(self, hashtag: str) -> response.TagInfoResponse: ...

    def get_story(self, hashtag: str) -> response.TagsStoryResponse: ...

    def get_section(self,
                    hashtag: str,
                    rank_token: str,
                    tab: str = None,
                    next_media_ids: List[int] = None,
                    max_id: str = None) -> response.TagFeedResponse: ...

    def search(self,
               query: str,
               exclude_list: List[int] = None,
               rank_token: str = None) -> response.SearchTagResponse: ...

    def follow(self, hashtag: str) -> response.GenericResponse: ...

    def unfollow(self, hashtag: str) -> response.GenericResponse: ...

    def get_related(self, hashtag: str) -> response.TagRelatedResponse: ...

    def get_feed(self, hashtag: str, rank_token: str, max_id: str = None) -> response.TagFeedResponse: ...

    def get_following(self, user_id: int) -> response.HashtagsResponse: ...

    def get_self_following(self) -> response.HashtagsResponse: ...

    def get_follow_suggestions(self) -> response.HashtagsResponse: ...

    def mark_story_media_seen(self,
                              hashtag_feed: response.TagFeedResponse,
                              items: List[Item]) -> response.MediaSeenResponse: ...
