from typing import Optional

from .collection import Collection

from .metadata import InternalMetadata


class Internal(Collection):
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
                            external_metadata: dict = None): ...

    def upload_photo_data(self, target_feed: int, internal_metadata: InternalMetadata): ...

    def configure_single_photo(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata,
                               external_metadata: dict = None): ...

    def upload_video(self,
                     target_feed: int,
                     video_filename: str,
                     internal_metadata: InternalMetadata = None): ...

    def upload_single_video(self,
                            target_feed: int,
                            video_filename: str,
                            internal_metadata: InternalMetadata = None,
                            external_metadata: dict = None): ...

    def upload_video_thumbnail(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata = None,
                               external_metadata: dict = None): ...

    def configure_single_video(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata = None,
                               external_metadata: dict = None): ...

    def configure_timeline_album(self,
                                 media: dict,
                                 internal_metadata: InternalMetadata,
                                 external_metadata: dict = None): ...

    def sync_device_features(self, prelogin: bool = False): ...

    def sync_user_features(self): ...

    def send_launcher_sync(self, prelogin: bool): ...

    def log_attribution(self): ...

    def log_resurrect_attribution(self): ...

    def read_msisdn_header(self, usage: str, subno_key: Optional[str] = None): ...

    def bootstrap_msisdn_header(self, usage: str = 'ig_select_app'): ...

    def fetch_zero_rating_token(self, reason: str = 'token_expired'): ...

    def get_megaphone_log(self): ...

    def get_facebook_hidden_search_entities(self): ...

    def get_facebook_ota(self): ...

    def get_loom_fetch_config(self): ...

    def get_profile_notice(self): ...

    def get_qp_fetch(self): ...

    def get_qp_cooldowns(self): ...

    def mark_story_media_seen(self, items: dict, source_id: Optional[str] = None, module: str = 'feed_timeline'): ...

    def configure_with_retries(self, configurator: function): ...
