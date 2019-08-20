from typing import Optional, Callable

import json

from instagram_api import response
from instagram_api.constants import Constants
from instagram_api.response.model import Token
from instagram_api.signatures import Signatures
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
                            external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def upload_photo_data(self, target_feed: int, internal_metadata: InternalMetadata):
        ...

    def configure_single_photo(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata,
                               external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def upload_video(self,
                     target_feed: int,
                     video_filename: str,
                     internal_metadata: InternalMetadata = None):
        ...

    def upload_single_video(self,
                            target_feed: int,
                            video_filename: str,
                            internal_metadata: InternalMetadata = None,
                            external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def upload_video_thumbnail(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata = None,
                               external_metadata: dict = None):
        ...

    def configure_single_video(self,
                               target_feed: int,
                               internal_metadata: InternalMetadata = None,
                               external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def configure_timeline_album(self,
                                 media: dict,
                                 internal_metadata: InternalMetadata,
                                 external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def sync_device_features(self, prelogin: bool = False) -> response.SyncResponse:
        request = self._ig.request('qe/sync/').add_headers(**{
            'X-DEVICE_ID': self._ig.uuid,
        }).add_posts(
            id=self._ig.uuid,
            experiments=Constants.LOGIN_EXPERIMENTS,
        )

        if prelogin:
            request.set_needs_auth(False)

        else:
            request.add_posts(
                _uuid=self._ig.uuid,
                _uid=self._ig.account_id,
                _csrftoken=self._ig.client.get_token(),
            )

        return request.get_response(response.SyncResponse)

    def sync_user_features(self) -> response.SyncResponse:
        ...

    def send_launcher_sync(self, prelogin: bool) -> response.LauncherSyncResponse:
        request = self._ig.request('launcher/sync/').add_posts(
            configs=Constants.LAUNCHER_CONFIGS,
        )

        if prelogin:
            request.set_needs_auth(False).add_posts(
                id=self._ig.uuid,
            )
        else:
            request.add_posts(
                id=self._ig.account_id,
                _uuid=self._ig.uuid,
                _uid=self._ig.account_id,
                _csrftoken=self._ig.client.get_token(),
            )

        return request.get_response(response.LauncherSyncResponse)

    def log_attribution(self) -> response.GenericResponse:
        return self._ig.request('attribution/log_attribution/').set_needs_auth(False).add_posts(
            adid=self._ig.advertising_id,
        ).get_response(response.GenericResponse)

    def log_resurrect_attribution(self) -> response.GenericResponse:
        ...

    def read_msisdn_header(self, usage: str, subno_key: Optional[str] = None) -> response.MsisdnHeaderResponse:
        request = self._ig.request('accounts/read_msisdn_header/').set_needs_auth(False).add_headers(**{
            'X-DEVICE-ID': self._ig.uuid,
        }).add_posts(
            device_id=self._ig.uuid,
            mobile_subno_usage=usage,
        )
        if subno_key is not None:
            request = request.add_posts(subno_key=subno_key)

        return request.get_response(response.MsisdnHeaderResponse)

    def bootstrap_msisdn_header(self, usage: str = 'ig_select_app') -> response.MsisdnHeaderResponse:
        ...

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
        request = self._ig.request('zr/token/result/').set_needs_auth(False).add_params(
            custom_device_id=self._ig.uuid,
            device_id=self._ig.device_id,
            fetch_reason=reason,
            # TODO: Если токена нет, None или ''???
            token_hash=self._ig.settings.get('zr_token', ''),
        )

        result = request.get_response(response.TokenResultResponse)
        self._save_zero_rating_token(result.token)

        return result

    def get_megaphone_log(self) -> response.MegaphoneLogResponse:
        ...

    def get_facebook_hidden_search_entities(self) -> response.FacebookHiddenEntitiesResponse:
        ...

    def get_facebook_ota(self) -> response.FacebookOTAResponse:
        return self._ig.request('facebook_ota/').add_params(
            fields=Constants.FACEBOOK_OTA_FIELDS,
            custom_user_id=self._ig.account_id,
            signed_body=Signatures.generate_signature('') + '.',
            ig_sig_key_version=Constants.SIG_KEY_VERSION,
            version_code=Constants.VERSOIN_CODE,
            version_name=Constants.IG_VERSION,
            custom_app_id=Constants.FACEBOOK_ORCA_APPLICATION_ID,
            custom_device_id=self._ig.uuid,
        ).get_response(response.FacebookOTAResponse)

    def get_loom_fetch_config(self) -> response.LoomFetchConfigResponse:
        return self._ig.request('loom/fetch_config/').get_response(response.LoomFetchConfigResponse)

    def get_profile_notice(self) -> response.ProfileNoticeResponse:
        return self._ig.request('users/profile_notice/').get_response(response.ProfileNoticeResponse)

    def get_qp_fetch(self) -> response.FetchQPDataResponse:
        query = (
            'viewer() {eligible_promotions.surface_nux_id(<surface>)'
            '.external_gating_permitted_qps(<external_gating_permitted_qps>)'
            '.supports_client_filters(true) {edges {priority,time_range {start,end},node'
            ' {id,promotion_id,max_impressions,triggers,contextual_filters {clause_type,filters'
            ' {filter_type,unknown_action,value {name,required,bool_value,int_value, string_value},extra_datas'
            ' {name,required,bool_value,int_value, string_value}},clauses {clause_type,filters'
            ' {filter_type,unknown_action,value {name,required,bool_value,int_value, string_value},extra_datas'
            ' {name,required,bool_value,int_value, string_value}},clauses {clause_type,filters'
            ' {filter_type,unknown_action,value {name,required,bool_value,int_value, string_value},extra_datas'
            ' {name,required,bool_value,int_value, string_value}},clauses {clause_type,filters'
            ' {filter_type,unknown_action,value {name,required,bool_value,int_value, string_value},extra_datas'
            ' {name,required,bool_value,int_value, string_value}}}}}},template {name,parameters'
            ' {name,required,bool_value,string_value,color_value,}},creatives {title {text},content'
            ' {text},footer {text},social_context {text},primary_action{title {text},url,limit,dismiss_promotion},'
            'secondary_action{title {text},url,limit,dismiss_promotion},dismiss_action{title'
            ' {text},url,limit,dismiss_promotion},image.scale(<scale>) {uri,width,height}}}}}}'
        )

        return self._ig.request('qp/batch_fetch/').add_posts(
            vc_policy='default',
            _csrftoken=self._ig.client.get_token(),
            _uid=self._ig.account_id,
            _uuid=self._ig.uuid,
            surfaces_to_queries=json.dumps({
                Constants.SURFACE_PARAM[0]: query,
                Constants.SURFACE_PARAM[1]: query,
            }),
            version=1,
            scale=2,
        ).get_response(response.FetchQPDataResponse)

    def get_qp_cooldowns(self) -> response.QPCooldownsResponse:
        ...

    def mark_story_media_seen(self,
                              items: dict,
                              source_id: Optional[str] = None,
                              module: str = 'feed_timeline') -> response.MediaSeenResponse:
        ...

    def configure_with_retries(self, configurator: Callable):
        ...
