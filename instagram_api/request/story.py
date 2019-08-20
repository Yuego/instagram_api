from typing import List

import json

from instagram_api import response
from instagram_api.constants import Constants
from instagram_api.response.model.item import Item

from .base import CollectionBase

__all__ = ['Story']


class Story(CollectionBase):

    def upload_photo(self, photo_filename: str, external_metadata: dict = None) -> response.ConfigureResponse: ...

    def upload_close_friends_photo(self,
                                   photo_filename: str,
                                   external_metadata: dict = None) -> response.ConfigureResponse: ...

    def upload_video(self, video_filename: str, external_metadata: dict = None) -> response.ConfigureResponse: ...

    def upload_close_friends_video(self,
                                   video_filename: str,
                                   external_metadata: dict = None) -> response.ConfigureResponse: ...

    def get_reels_tray_feed(self) -> response.ReelsTrayFeedResponse:
        return self._ig.request('feed/reels_tray/').set_signed_post(False).add_posts(
            supported_capabilities_new=json.dumps(Constants.SUPPORTED_CAPABILITIES),
            reason='pull_to_refresh',
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).get_response(response.ReelsTrayFeedResponse)

    def get_user_reel_media_feed(self, user_id: int) -> response.UserReelMediaFeedResponse: ...

    def get_user_story_feed(self, user_id: int) -> response.UserStoryFeedResponse: ...

    def get_reels_media_feed(self,
                             feed_list: List[int],
                             source: str = 'feed_timeline') -> response.ReelsMediaResponse: ...

    def get_archived_stories_feed(self) -> response.ArchivedStoriesFeedResponse: ...

    def get_story_item_viewers(self, story_pk: int, max_id: str = None) -> response.ReelMediaViewerResponse: ...

    def vote_poll_story(self, story_id: int, poll_id: int, voting_option: int) -> response.ReelMediaViewerResponse: ...

    def vote_slider_story(self,
                          story_id: int,
                          slider_id: int,
                          voting_option: int) -> response.ReelMediaViewerResponse: ...

    def get_story_poll_voters(self,
                              story_id: int,
                              poll_id: int,
                              voting_option: int,
                              max_id: str = None) -> response.StoryPollVotersResponse: ...

    def answer_story_question(self,
                              story_id: int,
                              question_id: int,
                              response_text: str) -> response.GenericResponse: ...

    def get_story_answers(self,
                          story_id: int,
                          question_id: int,
                          max_id: str = None) -> response.StoryAnswerResponse: ...

    def get_story_countdowns(self) -> response.StoryCountdownsResponse: ...

    def follow_story_countdown(self, countdown_id: int) -> response.GenericResponse: ...

    def unfollow_story_countdown(self, countdown_id: int) -> response.GenericResponse: ...

    def mark_media_seen(self, items: List[Item]) -> response.MediaSeenResponse: ...

    def get_reel_settings(self) -> response.ReelSettingsResponse: ...

    def set_reel_settings(self,
                          message_prefs: str,
                          allow_story_reshare: bool = None,
                          auto_archive: str = None) -> response.ReelSettingsResponse: ...
