from typing import Any

from instagram_api import request
from instagram_api.exceptions import InstagramException
from instagram_api.interfaces import ExperimentsInterface, InstagramInterface, ApiRequestInterface
from instagram_api.response.login import LoginResponse

from .client import Client
from .constants import Constants
from .devices import Device
from .request.base import ApiRequest
from .settings import StorageFactory, StorageHandler
from .signatures import Signatures

__all__ = ['Instagram']


class Instagram(ExperimentsInterface, InstagramInterface):
    account: request.Account
    business: request.Business
    collection: request.Collection
    creative: request.Creative
    direct: request.Direct
    discover: request.Discover
    hashtag: request.Hashtag
    highlight: request.Highlight
    tv: request.TV
    internal: request.Internal
    live: request.Live
    location: request.Location
    media: request.Media
    people: request.People
    push: request.Push
    shopping: request.Shopping
    story: request.Story
    timeline: request.Timeline
    usertag: request.Usertag

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
        self.tv = request.TV(self)
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

    def _login(self, username: str, password: str, force_login: bool, app_refresh_interval: int):
        assert username and password, 'You must provide a username and password to _login().'

        if self.username != username or self.password != password:
            self.change_user(username, password)

        if not self.is_maybe_logged_in or force_login:
            self._send_pre_login_flow()

            try:
                response = self.request(
                    'accounts/login/'
                ).require_auth(
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
                }).get_response(LoginResponse)
            except InstagramException as e:
                if e.has_response and e.response.is_two_factor_required:
                    return e.response
                else:
                    raise

            self._update_login_state(response)

            self._send_login_flow(True, app_refresh_interval)

            return response

        return self._send_login_flow(False, app_refresh_interval)

    def _send_login_flow(self, just_logged_in: bool, app_refresh_interval: int = 1800):
        assert isinstance(app_refresh_interval, int) and app_refresh_interval > 0, (
            'Instagram`s app state refresh interval must be a positive integer.'
        )
        assert app_refresh_interval < 21600, (
            'Instagram`s app state refresh interval is NOT allowed to be higher than 6 hours, and the lower is better!'
        )

        if just_logged_in:
            self.client.zero_rating.reset()

            self.internal.send_launcher_sync(False)

    def change_user(self, username: str, password: str):
        assert username and password, 'You must provide a username and password to change_user().'

        self.settings.change_user(username=username)

        saved_device_string = self.settings.get('device_string')
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

            self.settings.set('device_string', device_string)

            self.settings.set('device_id', Signatures.generate_device_id())
            self.settings.set('phone_id', Signatures.generate_uuid(keep_dashes=True))
            self.settings.set('uuid', Signatures.generate_uuid(keep_dashes=True))

            self.settings.set('account_id', None)

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
