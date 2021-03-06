from typing import Any, Optional, Union

import random

from datetime import timedelta
from time import time

from instagram_api import request, response as api_response
from instagram_api.exceptions import InstagramException, LoginRequiredException
from instagram_api.interfaces.api_request import ApiRequestInterface
from instagram_api.interfaces.experiments import ExperimentsInterface
from instagram_api.interfaces.instagram import InstagramInterface

from .client import Client
from .constants import Constants
from .devices import Device
from .request.request import ApiRequest
from .settings import StorageFactory, StorageHandler
from .signatures import Signatures

__all__ = ['Instagram']


class Instagram(ExperimentsInterface, InstagramInterface):

    def __init__(self, storage_config: dict, debug: bool = False, debug_truncate: bool = False):
        self.debug = debug
        self.debug_truncate = debug_truncate

        self.account = request.Account(self)
        self.business = request.Business(self)
        self.collection = request.Collection(self)
        self.creative = request.Creative(self)
        self.direct = request.Direct(self)
        self.discover = request.Discover(self)
        self.hashtag = request.Hashtag(self)
        self.highlight = request.Highlight(self)
        self.tv = request.Tv(self)
        self.internal = request.Internal(self)
        self.live = request.Live(self)
        self.location = request.Location(self)
        self.media = request.Media(self)
        self.people = request.People(self)
        self.push = request.Push(self)
        self.shopping = request.Shopping(self)
        self.story = request.Story(self)
        self.timeline = request.Timeline(self)
        self.usertag = request.Usertag(self)

        # TODO: test this
        def mix_self(this):
            def close_user(storage: StorageHandler):
                if isinstance(this.client, Client):
                    this.client.save_cookie_jar()

            return close_user

        self.settings = StorageFactory.create_handler(
            storage_config['storage_class'],
            storage_config['storage_config'],
            {
                StorageHandler.ON_CLOSE_USER: mix_self(self),
            },
        )

        self.client = Client(self)
        self.experiments = {}

    def login(self, username: str, password: str, app_refresh_interval: int = 1800):
        assert username and password, 'You must provide a username and password to login().'

        return self._login(username, password, False, app_refresh_interval)

    def _send_login_request(self) -> api_response.LoginResponse:
        response = self.request(
            'accounts/login/'
        ).set_needs_auth(
            False
        ).add_posts(**{
            'country_codes': [
                {
                    'country_code': 1,
                    'source': [
                        'default',
                        'sim',
                    ],
                },
            ],
            'phone_id': self.phone_id,
            '_csrftoken': self.client.get_token(),
            'username': self.username,
            'adid': self.advertising_id,
            'guid': self.uuid,
            'device_id': self.device_id,
            'password': self.password,
            'google_tokens': [],
            'login_attempt_count': 0
        }).get_response(api_response.LoginResponse)

        return response

    def _login(self, username: str, password: str, force_login: bool, app_refresh_interval: int):
        assert username and password, 'You must provide a username and password to _login().'

        if self.username != username or self.password != password:
            self.change_user(username, password)

        if not self.is_maybe_logged_in or force_login:
            self._send_pre_login_flow()

            try:
                response = self._send_login_request()
            except InstagramException as e:
                if e.has_response and e.response.is_two_factor_required:
                    return e.response
                else:
                    raise

            self._update_login_state(response)

            self._send_login_flow(True, app_refresh_interval)

            return response

        return self._send_login_flow(False, app_refresh_interval)

    def _update_login_state(self, response: api_response.LoginResponse):
        if not isinstance(response, api_response.LoginResponse) or not response.is_ok:
            raise ValueError('Invalid login response provided to `_update_login_state()`.')

        self.is_maybe_logged_in = True
        self.account_id = response.logged_in_user.pk
        self.settings.set('account_id', self.account_id)
        self.settings.set('last_login', time())

    def _send_pre_login_flow(self):

        self.client.zero_rating.reset()

        self.internal.read_msisdn_header('ig_select_app')
        self.internal.sync_device_features(True)
        self.internal.send_launcher_sync(True)
        self.internal.log_attribution()

        self.internal.fetch_zero_rating_token()
        self.account.set_contact_point_prefill('prefill')

    # TODO: перепроверить реализацию
    def _register_push_channels(self):
        last_fbns_token = self.settings.get('last_fbns_token')

        if last_fbns_token is None or last_fbns_token < (time() - timedelta(hours=24).total_seconds()):
            self.settings.set('fbns_token', None)

            return

        fbns_token = self.settings.get('fbns_token')

        if fbns_token is None:
            return

        try:
            self.push.register('mqtt', fbns_token)
        except Exception as e:
            self.settings.set('fbns_token', None)

    def _send_login_flow(self, just_logged_in: bool, app_refresh_interval: int = 1800):
        assert isinstance(app_refresh_interval, int) and app_refresh_interval > 0, (
            'Instagram`s app state refresh interval must be a positive integer.'
        )
        assert app_refresh_interval < 21600, (
            'Instagram`s app state refresh interval is NOT allowed to be higher than 6 hours, and the lower is better!'
        )
        """
        SUPER IMPORTANT:
        
        STOP trying to ask us to remove this code section!
        
        EVERY time the user presses their device's home button to leave the
        app and then comes back to the app, Instagram does ALL of these things
        to refresh its internal app state. We MUST emulate that perfectly,
        otherwise Instagram will silently detect you as a "fake" client
        after a while!
        
        You can configure the login's $appRefreshInterval in the function
        parameter above, but you should keep it VERY frequent (definitely
        NEVER longer than 6 hours), so that Instagram sees you as a real
        client that keeps quitting and opening their app like a REAL user!
        
        Otherwise they WILL detect you as a bot and silently BLOCK features
        or even ban you.
        
        You have been warned.
        """

        if just_logged_in:
            self.client.zero_rating.reset()

            self.internal.send_launcher_sync(False)
            self.internal.sync_user_features()
            self.timeline.get_timeline_feed(None, {'recover_from_crash': True})
            self.story.get_reels_tray_feed()
            self.discover.get_suggested_searches('users')
            self.discover.get_recent_searches()
            self.discover.get_suggested_searches('blended')

            self.internal.fetch_zero_rating_token()
            self._register_push_channels()
            self.direct.get_ranked_recipients('reshare', True)
            self.direct.get_ranked_recipients('raven', True)
            self.direct.get_inbox()

            self.direct.get_presences()
            self.people.get_recent_activity_inbox()
            self.internal.get_loom_fetch_config()
            self.internal.get_profile_notice()
            self.media.get_blocked_media()

            self.people.get_bootstrap_users()

            self.discover.get_explore_feed(None, True)

            self.internal.get_qp_fetch()
            self.internal.get_facebook_ota()
        else:
            last_login_time = self.settings.get('last_login')
            is_session_expired = last_login_time is None or (time() - last_login_time) > app_refresh_interval

            try:
                self.timeline.get_timeline_feed(None, {
                    'is_pull_to_refresh': None if is_session_expired else random.random() * 4 < 3
                })
            except LoginRequiredException as e:
                return self._login(self.username, self.password, True, app_refresh_interval)

            if is_session_expired:
                self.settings.set('last_login', time())

                self.session_id = Signatures.generate_uuid(True)
                self.settings.set('session_id', self.session_id)

                self.people.get_bootstrap_users()
                self.story.get_reels_tray_feed()
                self.direct.get_ranked_recipients('reshare', True)
                self.direct.get_ranked_recipients('raven', True)
                self._register_push_channels()

                self.direct.get_inbox()
                self.direct.get_presences()
                self.people.get_recent_activity_inbox()
                self.internal.get_profile_notice()
                self.discover.get_explore_feed()

            last_experiments_time = self.settings.get('last_experiments')
            if last_experiments_time is None or (time() - last_experiments_time) > self.EXPERIMENTS_REFRESH:
                self.internal.sync_user_features()
                self.internal.sync_device_features()

            expired = time() - self.settings.get('zr_expires')
            if expired > 0:
                self.client.zero_rating.reset()
                self.internal.fetch_zero_rating_token('token_stale' if expired > 7200 else 'token_expired')

        self.client.save_cookie_jar()

    def logout(self):
        response = self.request('accounts/logout').set_signed_post(False).add_posts(**{
            'phone_id': self.phone_id,
            '_csrftoken': self.client.get_token(),
            'guid': self.uuid,
            'device_id': self.device_id,
            '_uuid': self.uuid,
        }).get_response(api_response.LogoutResponse)

        self.client.save_cookie_jar()

        return response

    def change_user(self, username: str, password: str):
        assert username and password, 'You must provide a username and password to set_active_user().'

        self.settings.set_active_user(username=username)

        saved_device_string = self.settings.get('devicestring')
        self.device = Device(
            app_version=Constants.IG_VERSION,
            version_code=Constants.VERSOIN_CODE,
            user_locale=Constants.USER_AGENT_LOCALE,
            device_string=saved_device_string,
        )

        device_string = self.device.device_string

        reset_cookie_jar = False
        if (
                device_string != saved_device_string
                or not self.settings.get('uuid')
                or not self.settings.get('phone_id')
                or not self.settings.get('device_id')
        ):
            self.settings.erase_device_settings()

            self.settings.set('devicestring', device_string)

            self.settings.set('device_id', Signatures.generate_device_id())
            self.settings.set('phone_id', Signatures.generate_uuid(keep_dashes=True))
            self.settings.set('uuid', Signatures.generate_uuid(keep_dashes=True))

            self.settings.set('account_id', '')

            reset_cookie_jar = True

        if self.settings.get('advertising_id') is None:
            self.settings.set('advertising_id', Signatures.generate_uuid(keep_dashes=True))

        if self.settings.get('session_id') is None:
            self.settings.set('session_id', Signatures.generate_uuid(keep_dashes=True))

        self.username = username
        self.password = password

        self.uuid = self.settings.get('uuid')
        self.advertising_id = self.settings.get('advertising_id')
        self.device_id = self.settings.get('device_id')
        self.phone_id = self.settings.get('phone_id')
        self.session_id = self.settings.get('session_id')
        self.experiments = self.settings.get_experiments()

        if not reset_cookie_jar and self.settings.is_maybe_logged_in():
            self.is_maybe_logged_in = True
            self.account_id = self.settings.get('account_id')

        else:
            self.is_maybe_logged_in = False
            self.account_id = None

        self.client.update_from_current_settings(reset_cookie_jar=reset_cookie_jar)

        if self.client.get_token() is None:
            self.is_maybe_logged_in = False

    def request(self, url: str) -> ApiRequestInterface:
        return ApiRequest(self, url)

    def is_experiment_enabled(self, experiment: str, param: str, default: bool = False):
        param = self.experiments.get(experiment, {}).get(param, None)
        if param is not None:
            return param in ['enabled', 'true', '1']
        else:
            return default

    def get_experiment_param(self, experiment: str, param: str, default: Any = None):
        return self.experiments.get(experiment, {}).get(param, default)

    def finish_two_factor_login(self,
                                username: str,
                                password: str,
                                two_factor_identifier: str,
                                verification_code: str,
                                verification_method: int,
                                app_refresh_interval: int = 1800,
                                username_handler: str = None):
        raise NotImplementedError

    def get_proxy(self):
        raise NotImplementedError

    def get_verify_ssl(self):
        raise NotImplementedError

    def send_two_factor_login_sms(self,
                                  username: str,
                                  password: str,
                                  two_factor_identifier: str,
                                  username_handler: str = None):
        raise NotImplementedError

    def set_proxy(self, proxy: Optional[Union[str, dict, list]]):
        raise NotImplementedError

    def set_verify_ssl(self, state: Union[bool, str]):
        raise NotImplementedError
