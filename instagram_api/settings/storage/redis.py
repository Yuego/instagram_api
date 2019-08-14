import json
import redis

from instagram_api.exceptions.settings import SettingsException
from .base import StorageBase

"""

REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'socket_timeout': 2,
}

"""
__all__ = ['RedisStorage']


class RedisStorage(StorageBase):

    # Easy mock Redis
    redis_class = redis.StrictRedis

    _redis = None

    def open(self, config: dict):
        super(RedisStorage, self).open(config=config)

        self._redis = self.redis_class(**config)

    def close(self):
        self._redis = None

    def _set_user_key(self, username, key, value, trigger_key=None):
        self._redis.set(self._user_key(username, key), value)

    def _get_user_key(self, username, key):
        return self._redis.get(self._user_key(username, key))

    def _del_user_key(self, username, key):
        return self._redis.delete(self._user_key(username, key))

    def _pack_settings_dict(self, settings: dict):
        return json.dumps(settings)

    def _unpack_settings_dict(self, settings: str):
        return json.loads(settings)

    def has_user(self, username: str):
        return self._redis.exists(self._user_key(username, 'settings')) > 0

    def has_user_cookies(self):
        return self._redis.exists(self._user_key(self._username, 'cookies')) > 0
