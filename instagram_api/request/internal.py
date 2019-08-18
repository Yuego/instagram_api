from typing import Optional

from instagram_api import response
from .base import CollectionBase
from .metadata import InternalMetadata


class Internal(CollectionBase):
    # @var int Number of retries for each video chunk. */
    MAX_CHUNK_RETRIES = 5

    # @var int Number of retries for resumable uploader. */
    MAX_RESUMABLE_RETRIES = 15

    # @var int Number of retries for each media configuration. */
    MAX_CONFIGURE_RETRIES = 5

    # @var int Minimum video chunk size in bytes. */
    MIN_CHUNK_SIZE = 204800

    # @var int Maximum video chunk size in bytes. */
    MAX_CHUNK_SIZE = 5242880

    def upload_single_photo(self,
                            target_feed: int,
                            photo_filename: str,
                            internal_metadata: InternalMetadata = None,
                            external_metadata: dict = None) -> response.ConfigureResponse: ...

    def upload_photo_data(self, target_feed: int, internal_metadata: InternalMetadata): ...

    def configure_single_photo(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata,
                               external_metadata: dict = None) -> response.ConfigureResponse: ...

    def upload_video(self,
                     target_feed: int,
                     video_filename: str,
                     internal_metadata: InternalMetadata = None): ...

    def upload_single_video(self,
                            target_feed: int,
                            video_filename: str,
                            internal_metadata: InternalMetadata = None,
                            external_metadata: dict = None) -> response.ConfigureResponse: ...

    def upload_video_thumbnail(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata = None,
                               external_metadata: dict = None): ...

    def configure_single_video(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata = None,
                               external_metadata: dict = None) -> response.ConfigureResponse: ...

    def configure_timeline_album(self,
                                 media: dict,
                                 internal_metadata: InternalMetadata,
                                 external_metadata: dict = None) -> response.ConfigureResponse: ...

    def sync_device_features(self, prelogin: bool = False) -> response.SyncResponse: ...

    def sync_user_features(self) -> response.SyncResponse: ...

    def send_launcher_sync(self, prelogin: bool) -> response.LauncherSyncResponse: ...

    def log_attribution(self) -> response.GenericResponse: ...

    def log_resurrect_attribution(self) -> response.GenericResponse: ...

    def read_msisdn_header(self, usage: str, subno_key: Optional[str] = None) -> response.MsisdnHeaderResponse: ...

    def bootstrap_msisdn_header(self, usage: str = 'ig_select_app') -> response.MsisdnHeaderResponse: ...

    def fetch_zero_rating_token(self, reason: str = 'token_expired') -> response.TokenResultResponse: ...

    def get_megaphone_log(self) -> response.MegaphoneLogResponse: ...

    def get_facebook_hidden_search_entities(self) -> response.FacebookHiddenEntitiesResponse: ...

    def get_facebook_ota(self) -> response.FacebookOTAResponse: ...

    def get_loom_fetch_config(self) -> response.LoomFetchConfigResponse: ...

    def get_profile_notice(self) -> response.ProfileNoticeResponse: ...

    def get_qp_fetch(self) -> response.FetchQPDataResponse: ...

    def get_qp_cooldowns(self) -> response.QPCooldownsResponse: ...

    def mark_story_media_seen(self,
                              items: dict,
                              source_id: Optional[str] = None,
                              module: str = 'feed_timeline') -> response.MediaSeenResponse: ...

    def configure_with_retries(self, configurator: function): ...
