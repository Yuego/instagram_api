from typing import List

from instagram_api import response

from .base import CollectionBase

__all__ = ['Usertag']


class Usertag(CollectionBase):

    def tag_media(self,
                  media_id: str,
                  user_id: int,
                  position: List[float],
                  caption_text: str = '') -> response.EditMediaResponse: ...

    def untag_media(self,
                    media_id: str,
                    user_id: int,
                    caption_text: str = '') -> response.EditMediaResponse: ...

    def remove_self_tag(self, media_id: str) -> response.MediaInfoResponse: ...

    def get_user_feed(self, user_id: int, max_id: str = None) -> response.UsertagsResponse: ...

    def get_self_user_feed(self, max_id: str = None) -> response.UsertagsResponse: ...

    def set_review_preference(self, enabled: bool) -> response.ReviewPreferenceResponse: ...
