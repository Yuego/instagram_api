from typing import Optional, Callable

from instagram_api import response
from instagram_api.constants import Constants
from instagram_api.response.model import Token
from instagram_api.exceptions import SettingsException
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

    def sync_device_features(self, prelogin: bool = False) -> response.SyncResponse:
        request = self._ig.request('qe/sync/').add_headers(**{
            'X-DEVICE_ID': self._ig.uuid,
        }).add_posts(**{
            'id': self._ig.uuid,
            'experiments': Constants.LOGIN_EXPERIMENTS,
        })

        if prelogin:
            request.set_needs_auth(False)

        else:
            request.add_posts(**{
                '_uuid': self._ig.uuid,
                '_uid': self._ig.account_id,
                '_csrftoken': self._ig.client.get_token(),
            })

        return request.get_response(response.SyncResponse)

    def sync_user_features(self) -> response.SyncResponse: ...

    def send_launcher_sync(self, prelogin: bool) -> response.LauncherSyncResponse:
        request = self._ig.request('launcher/sync/').add_posts(**{
            'configs': Constants.LAUNCHER_CONFIGS,
        })

        if prelogin:
            request.set_needs_auth(False).add_posts(**{
                'id': self._ig.uuid,
            })
        else:
            request.add_posts(**{
                'id': self._ig.account_id,
                '_uuid': self._ig.uuid,
                '_uid': self._ig.account_id,
                '_csrftoken': self._ig.client.get_token(),
            })

        return request.get_response(response.LauncherSyncResponse)

    def log_attribution(self) -> response.GenericResponse:
        return self._ig.request('attribution/log_attribution/').set_needs_auth(False).add_posts(**{
            'adid': self._ig.advertising_id,
        }).get_response(response.GenericResponse)

    def log_resurrect_attribution(self) -> response.GenericResponse: ...

    def read_msisdn_header(self, usage: str, subno_key: Optional[str] = None) -> response.MsisdnHeaderResponse:
        request = self._ig.request('accounts/read_msisdn_header/').set_needs_auth(False).add_headers(**{
            'X-DEVICE-ID': self._ig.uuid,
        }).add_posts(**{
            'device_id': self._ig.uuid,
            'mobile_subno_usage': usage,
        })
        if subno_key is not None:
            request = request.add_posts(**{
                'subno_key': subno_key,
            })

        return request.get_response(response.MsisdnHeaderResponse)

    def bootstrap_msisdn_header(self, usage: str = 'ig_select_app') -> response.MsisdnHeaderResponse: ...

    def _save_zero_rating_token(self, token: Optional[Token]):
        if token is None:
            return

        rules = {}
        for rule in token.rewrite_rules:
            rules[rule.matcher] = rule.replacer

        self._ig.client.zero_rating.update(rules)

        try:
            self._ig.settings.set_rewrite_rules(rules)
            self._ig.settings.set('zr_token', token.token_hash)
            self._ig.settings.set('zr_expires', token.expires_at)

        except SettingsException as e:
            pass

    def fetch_zero_rating_token(self, reason: str = 'token_expired') -> response.TokenResultResponse:
        request = self._ig.request('zr/token/result/').set_needs_auth(False).add_params(**{
            'custom_device_id': self._ig.uuid,
            'device_id': self._ig.device_id,
            'fetch_reason': reason,
            # TODO: Если токена нет, None или ''???
            'token_hash': self._ig.settings.get('zr_token'),
        })

        result = request.get_response(response.TokenResultResponse)
        self._save_zero_rating_token(result.token)

        return result

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

    def configure_with_retries(self, configurator: Callable): ...
