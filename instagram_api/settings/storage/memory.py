from .base import StorageBase

__all__ = ['MemoryStorage']


class MemoryStorage(StorageBase):
    _data = {}

    def close(self):
        self._data = {}

    def _get_user_key(self, username: str, key: str):
        return self._data.get(self._user_key(username, key), None)

    def _set_user_key(self, username: str, key: str, value):
        self._data[self._user_key(username, key)] = value

    def _del_user_key(self, username: str, key: str):
        key_name = self._user_key(username, key)
        return self._data.pop(key_name, None)

    def has_user(self, username: str):
        return self._user_key(username, 'settings') in self._data

    def has_user_cookies(self):
        return self._user_key(self._username, 'cookies') in self._data
