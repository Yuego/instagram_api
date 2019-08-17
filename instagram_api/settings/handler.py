from http.cookiejar import CookieJar

from instagram_api.exceptions.settings import SettingsException
from instagram_api.interfaces import StorageHandlerInterface, StorageInterface

__all__ = ['StorageHandler']


class StorageHandler(StorageHandlerInterface):
    PERSISTENT_KEYS = [
        'account_id',  # The numerical UserPK ID of the account.
        'devicestring',  # Which Android device they're identifying as.
        'device_id',  # Hardware identifier.
        'phone_id',  # Hardware identifier.
        'uuid',  # Universally unique identifier.
        'advertising_id',  # Google Play advertising ID.
        'session_id',  # The user's current application session ID.
        'experiments',  # Interesting experiment variables for this account.
        'fbns_auth',  # Serialized auth credentials for FBNS.
        'fbns_token',  # Serialized FBNS token.
        'last_fbns_token',  # Tracks time elapsed since our last FBNS token refresh.
        'last_login',  # Tracks time elapsed since our last login state refresh.
        'last_experiments',  # Tracks time elapsed since our last experiments refresh.
        'datacenter',  # Preferred data center (region-based).
        'presence_disabled',  # Whether the presence feature has been disabled by user.
        'zr_token',  # Zero rating token.
        'zr_expires',  # Zero rating token expiration Timestamp.
        'zr_rules',  # Zero rating rewrite rules.
    ]

    KEEP_KEYS_WHEN_ERASING_DEVICE = [
        'account_id',  # We don't really need to keep this, but it's a good example.
    ]

    EXPERIMENT_KEYS = [
        'ig_android_2fac',
        'ig_android_realtime_iris',
        'ig_android_skywalker_live_event_start_end',
        'ig_android_gqls_typing_indicator',
        'ig_android_upload_reliability_universe',
        'ig_android_photo_fbupload_universe',
        'ig_android_video_segmented_upload_universe',
        'ig_android_direct_video_segmented_upload_universe',
        'ig_android_reel_raven_video_segmented_upload_universe',
        'ig_android_ad_async_ads_universe',
        'ig_android_direct_inbox_presence',
        'ig_android_direct_thread_presence',
        'ig_android_rtc_reshare',
        'ig_android_sidecar_photo_fbupload_universe',
        'ig_android_fbupload_sidecar_video_universe',
        'ig_android_skip_get_fbupload_photo_universe',
        'ig_android_skip_get_fbupload_universe',
        'ig_android_live_suggested_live_expansion',
        'ig_android_live_qa_broadcaster_v1_universe',
    ]

    _storage: StorageInterface
    _callbacks: dict
    _username: str
    _user_settings: dict

    def __init__(self, storage: StorageInterface, storage_config: dict, callbacks: dict = None):
        self._username = None
        self._user_settings = {}

        callbacks = callbacks or {}

        if not isinstance(storage, StorageInterface):
            raise SettingsException('You must provide an instance of a StorageInterface class')

        if not isinstance(storage_config, dict):
            raise SettingsException('The storage config must be a dict instance')

        self._callbacks = callbacks

        self._storage = storage
        self._storage.open(storage_config)

    def __del__(self):
        if self._username is not None:
            self._trigger_callback(self.ON_CLOSE_USER)
            self._storage.close_user()
            self._username = None

        self._storage.close()

    def has_user(self, username: str) -> bool:
        self._validate_empty_value(username)

        return self._storage.has_user(username)

    def move_user(self, old_username: str, new_username: str):
        self._validate_empty_value(old_username)
        self._validate_empty_value(new_username)

        if self._username in [old_username, new_username]:
            raise SettingsException('Attempted to move settings to/from the currently active user.')

        self._storage.move_user(old_username, new_username)

    def delete_user(self, username: str):
        self._validate_empty_value(username)

        if username == self._username:
            raise SettingsException('Attempted to delete the currently active user.')

        self._storage.delete_user(username)

    def select_user(self, username: str):
        self._validate_empty_value(username)

        if username == self._username:
            return

        if self._username is not None:
            self._trigger_callback(self.ON_CLOSE_USER)
            self._storage.close_user()

        self._username = username
        self._user_settings = {}
        self._storage.open_user(username)

        in_storage_settings = self._storage.load_user_settings()
        for key, value in in_storage_settings:
            if key == 'username_id':
                key = 'account_id'

            if key == 'adid':
                key = 'advertising_id'

            if key in self.PERSISTENT_KEYS:
                self._user_settings[key] = value

    def is_maybe_logged_in(self) -> bool:
        self._validate_user_is_active()

        return self._storage.has_user_cookies() and self.get('account_id', None) is not None

    def erase_device_settings(self):
        for key in self.PERSISTENT_KEYS:
            if key not in self.KEEP_KEYS_WHEN_ERASING_DEVICE:
                self.set(key, '')

        self.set_cookies(self._storage.cookie_jar_class())

    def get(self, key: str, default=None):
        self._validate_user_is_active()

        if key not in self.PERSISTENT_KEYS:
            raise SettingsException(f'The settings key "{key}" is not a valid persistent key name.')

        key = self._user_settings.get(key, default)
        return key if key else default

    def set(self, key: str, value):
        self._validate_user_is_active()

        if key not in self.PERSISTENT_KEYS:
            raise SettingsException(f'The settings key "{key}" is not a valid persistent key name.')

        if value is None:
            raise SettingsException(f'Illegal attempt to store null value in settings storage')

        if key not in self._user_settings or self._user_settings[key] != value:
            self._user_settings[key] = value
            self._storage.save_user_settings(self._user_settings, key)

    def has_cookies(self):
        self._validate_user_is_active()

        return self._storage.has_user_cookies()

    def get_cookies(self):
        self._validate_user_is_active()

        return self._storage.load_user_cookies()

    def set_cookies(self, jar: CookieJar):
        self._validate_user_is_active()

        self._storage.save_user_cookies(jar)

    def reset_cookies(self):
        self._storage.save_user_cookies(self._storage.cookie_jar_class())

    def set_rewrite_rules(self, rules: dict):
        self.set('zr_rules', rules)

    def get_rewrite_rules(self):
        return self.get('zr_rules', {})

    def _trigger_callback(self, callback_name: str):
        if callback_name not in self.SUPPORTED_CALLBACKS:
            raise SettingsException(f'The string "{callback_name}" is not a valid callback name.')

        if callback_name in self._callbacks:
            self._callbacks[callback_name](self)

    @staticmethod
    def _validate_empty_value(value):
        if not isinstance(value, str) or not value:
            raise SettingsException('Parameter must be non-empty string')

    @staticmethod
    def _validate_string(value):
        if not isinstance(value, str):
            raise SettingsException('Parameter must be string')

    def _validate_user_is_active(self):
        if self._username is None:
            raise SettingsException('Called user-related function before setting the current storage user.')
