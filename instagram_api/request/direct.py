from typing import Optional, List

from instagram_api import response

from .base import CollectionBase

__all__ = ['Direct']


class Direct(CollectionBase):

    def get_inbox(self, cursor_id: Optional[str] = None) -> response.DirectInboxResponse: ...

    def get_pending_inbox(self, cursor_id: Optional[str] = None) -> response.DirectPendingInboxResponse: ...

    def approve_pending_threads(self, threads: list) -> response.GenericResponse: ...

    def decline_pending_threads(self, threads: list) -> response.GenericResponse: ...

    def decline_all_pending_threads(self) -> response.GenericResponse: ...

    def get_presences(self) -> response.PresencesResponse: ...

    def get_ranked_recipients(self,
                              mode: str,
                              show_threads: bool,
                              query: str = None) -> response.DirectRankedRecipientsResponse: ...

    def get_thread_by_participants(self, users: List[int]) -> response.DirectThreadResponse: ...

    def get_thread(self, thread_id: int, cursor_id: Optional[str] = None) -> response.DirectThreadResponse: ...

    def get_visual_thread(self,
                          thread_id: int,
                          cursor_id: Optional[str] = None) -> response.DirectVisualThreadResponse: ...

    def update_thread_title(self, thread_id: int, title: str) -> response.DirectThreadResponse: ...

    def mute_thread(self, thread_id: int) -> response.GenericResponse: ...

    def unmute_thread(self, thread_id: int) -> response.GenericResponse: ...

    def create_group_thread(self,
                            user_ids: List[int],
                            thread_title: str) -> response.DirectCreateGroupThreadResponse: ...

    def add_users_to_thread(self, thread_id: int, users: List[int]) -> response.DirectThreadResponse: ...

    def leave_thread(self, thread_id: int) -> response.GenericResponse: ...

    def hide_thread(self, thread_id: int) -> response.GenericResponse: ...

    def send_text(self, recipients: list, text: str, options: dict = None) -> response.DirectSendItemResponse: ...

    def send_post(self, recipients: list, media_id: int, options: dict = None) -> response.DirectSendItemsResponse: ...

    def send_photo(self,
                   recipients: list,
                   photo_filename: str,
                   options: dict = None) -> response.DirectSendItemResponse: ...

    def send_disappearing_photo(self,
                                recipients: list,
                                photo_filename: str,
                                external_metadata: dict = None) -> response.ConfigureResponse: ...

    def send_replayable_photo(self,
                              recipients: list,
                              photo_filename: str,
                              external_metadata: dict = None) -> response.ConfigureResponse: ...

    def send_video(self,
                   recipients: list,
                   video_filename: str,
                   options: dict = None) -> response.DirectSendItemResponse: ...

    def send_disappearing_video(self,
                                recipients: list,
                                video_filename: str,
                                external_metadata: dict = None) -> response.ConfigureResponse: ...

    def send_replayable_video(self,
                              recipients: list,
                              video_filename: str,
                              external_metadata: dict = None) -> response.ConfigureResponse: ...

    def send_like(self, recipients: list, options: dict = None) -> response.DirectSendItemResponse: ...

    def send_hashtag(self, recipients: list, hashtag: str, options: dict = None) -> response.DirectSendItemResponse: ...

    def send_location(self,
                      recipients: list,
                      location_id: int,
                      options: dict = None) -> response.DirectSendItemResponse: ...

    def send_profile(self,
                     recipients: list,
                     user_id: int,
                     options: dict = None) -> response.DirectSendItemResponse: ...

    def send_reaction(self,
                      thread_id: int,
                      thread_item_id: int,
                      reaction_type: str,
                      options: dict = None) -> response.DirectSendItemResponse: ...

    def send_story(self,
                   recipients: list,
                   story_id: int,
                   reel_id: int = None,
                   options: dict = None) -> response.DirectSendItemsResponse: ...

    def send_live(self,
                  recipients: list,
                  broadcast_id: int,
                  options: dict = None) -> response.DirectSendItemResponse: ...

    def delete_reaction(self,
                        thread_id: int,
                        thread_item_id: int,
                        reaction_type: str,
                        options: dict = None) -> response.DirectSendItemResponse: ...

    def delete_item(self, thread_id: int, thread_item_id: int) -> response.GenericResponse: ...

    def mark_item_seen(self, thread_id: int, thread_item_id: int) -> response.DirectSendItemResponse: ...

    def mark_visual_items_seen(self, thread_id: int, thread_item_ids: List[int]) -> response.GenericResponse: ...

    def mark_visual_items_replayed(self, thread_id: int, thread_item_ids: List[int]) -> response.GenericResponse: ...
