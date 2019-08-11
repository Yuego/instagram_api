import redis

from instagram_api.exceptions.settings import SettingsException
from .interface import StorageInterface

"""

REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'socket_timeout': 2,
}

"""


class RedisStorage(StorageInterface):

    _redis = None
    _prefix = 'ig_'

    _username = None

    def open(self, config: dict):
        self._prefix = config.pop('prefix', 'ig_')

        self._redis = redis.StrictRedis(**config)

    def close(self):
        self._redis = None

    def _user_key(self, username: str, key: str):
        return f'{self._prefix}{username}_{key}'

    def _set_user_key(self, username, key, value):
        self._redis.set(self._user_key(username, key), value)

    def _get_user_key(self, username, key):
        return self._redis.get(self._user_key(username, key))

    def _del_user_key(self, username, key):
        return self._redis.delete(self._user_key(username, key))

    def has_user(self, username: str):
        return self._redis.exists(self._user_key(username, 'settings')) > 0

    def open_user(self, username: str):
        self._username = username

    def close_user(self):
        self._username = None

    def move_user(self, old_username: str, new_username: str):
        if not self.has_user(old_username):
            raise SettingsException(f'Cannot move non-existent user {old_username}')

        if self.has_user(new_username):
            raise SettingsException(f'Refusing to owerwrite existing user data {new_username}')

        settings = self._get_user_key(old_username, 'settings')
        cookies = self._get_user_key(old_username, 'cookies')

        self._set_user_key(new_username, 'settings', settings)
        if cookies is not None:
            self._set_user_key(new_username, 'cookies', cookies)

        self.delete_user(old_username)

    def delete_user(self, username: str):
        self._del_user_key(username, 'settings')
        self._del_user_key(username, 'cookies')

    def load_user_settings(self):
        return self._get_user_key(self._username, 'settings')

    def save_user_settings(self, settings: dict, trigger_key: str = None):
        self._set_user_key(self._username, 'settings', settings)

    def has_user_cookies(self):
        return self._redis.exists(self._user_key(self._username, 'cookies')) > 0

    def load_user_cookies(self):
        return self._get_user_key(self._username, 'cookies')

    def save_user_cookies(self, data: dict):
        self._set_user_key(self._username, 'cookies', data)
