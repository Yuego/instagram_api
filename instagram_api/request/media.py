from typing import List

from instagram_api import response

from .base import CollectionBase


class Media(CollectionBase):

    def get_info(self, media_id: str) -> response.MediaInfoResponse: ...

    def delete(self, media_id: str, media_type='PHOTO') -> response.MediaDeleteResponse: ...

    def edit(self,
             media_id: str,
             caption_text: str = '',
             metadata: dict = None,
             media_type: str = 'PHOTO') -> response.EditMediaResponse: ...

    def like(self,
             media_id: str,
             module: str = 'feed_timeline',
             extra_data: dict = None) -> response.GenericResponse: ...

    def unlike(self,
               media_id: str,
               module: str = 'feed_timeline',
               extra_data: dict = None) -> response.GenericResponse: ...

    def get_liked_feed(self, max_id: str = None) -> response.LikeFeedResponse: ...

    def get_likers(self, media_id: str) -> response.MediaLikersResponse: ...

    def get_likers_group(self, media_id: str) -> response.MediaLikersResponse: ...

    def enable_comments(self, media_id: str) -> response.GenericResponse: ...

    def disable_comments(self, media_id: str) -> response.GenericResponse: ...

    def comment(self,
                media_id: str,
                comment_text: str,
                reply_comment_id: int = None,
                module: str = 'comments_v2') -> response.CommentResponse: ...

    def get_comments(self, media_id: str, options: dict = None) -> response.MediaCommentsResponse: ...

    def get_comment_replies(self,
                            media_id: str,
                            comment_id: int,
                            options: dict = None) -> response.MediaCommentRepliesResponse: ...

    def delete_comment(self, media_id: str, comment_id: int) -> response.DeleteCommentResponse: ...

    def delete_comments(self, media_id: str, comment_ids: List[int]) -> response.DeleteCommentResponse: ...

    def like_comment(self, comment_id: int) -> response.CommentLikeUnlikeResponse: ...

    def unlike_comment(self, comment_id: int) -> response.CommentLikeUnlikeResponse: ...

    def get_comment_likers(self, comment_id: int) -> response.CommentLikersResponse: ...

    def translate_comments(self, comment_ids: List[int]) -> response.TranslateResponse: ...

    def validate_url(self, url: str) -> response.ValidateURLResponse: ...

    def save(self, media_id: str) -> response.SaveAndUnsaveMediaResponse: ...

    def unsave(self, media_id: str) -> response.SaveAndUnsaveMediaResponse: ...

    def get_saved_feed(self, max_id: str = None) -> response.SavedFeedResponse: ...

    def get_blocked_media(self) -> response.BlockedMediaResponse: ...

    def report(self, media_id: str, source_name: str = 'feed_contextual_chain') -> response.GenericResponse: ...

    def report_comment(self, media_id: str, comment_id: int) -> response.GenericResponse: ...

    def get_permalink(self, media_id: str) -> response.PermalinkResponse: ...
