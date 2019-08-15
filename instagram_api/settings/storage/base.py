import json

from abc import abstractmethod

from requests.utils import dict_from_cookiejar, cookiejar_from_dict

from instagram_api.exceptions.settings import SettingsException
from instagram_api.interfaces import StorageInterface
from instagram_api.utils.http import ClientCookieJar

__all__ = ['StorageBase']

_default_prefix = '_ig'


class StorageBase(StorageInterface):
    cookie_jar_class = ClientCookieJar

    _prefix: str = _default_prefix
    _username: str = None

    def open(self, config: dict):
        config = config or {}

        prefix = config.pop('prefix', _default_prefix)

        if prefix is None:
            prefix = ''

        self._prefix = prefix

    def _user_key(self, username: str, key: str):
        return f'{self._prefix}{username}_{key}'

    @abstractmethod
    def _get_user_key(self, username: str, key: str):
        raise NotImplementedError

    @abstractmethod
    def _set_user_key(self, username: str, key: str, value, trigger_key: str = None):
        raise NotImplementedError

    @abstractmethod
    def _del_user_key(self, username: str, key: str):
        raise NotImplementedError

    @abstractmethod
    def _pack_settings_dict(self, settings: dict) -> str:
        raise NotImplementedError

    @abstractmethod
    def _unpack_settings_dict(self, settings: str) -> dict:
        raise NotImplementedError

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
        if self._username is None:
            raise SettingsException(f'Empty username. You forgot to call `open_user`?')

        settings = self._get_user_key(self._username, 'settings')

        if settings is None:
            return None

        return self._unpack_settings_dict(settings)

    def save_user_settings(self, settings: dict, trigger_key: str = None):
        if self._username is None:
            raise SettingsException(f'Empty username. You forgot to call `open_user`?')

        packed_settings = self._pack_settings_dict(settings)

        self._set_user_key(self._username, 'settings', packed_settings, trigger_key)

    def load_user_cookies(self):
        if self._username is None:
            raise SettingsException(f'Empty username. You forgot to call `open_user`?')

        jar_string = self._get_user_key(self._username, 'cookies')

        if jar_string is None:
            return None

        jar_dict = json.loads(jar_string)

        return cookiejar_from_dict(jar_dict, self.cookie_jar_class())

    def save_user_cookies(self, jar: ClientCookieJar):
        if self._username is None:
            raise SettingsException(f'Empty username. You forgot to call `open_user`?')

        jar_dict = dict_from_cookiejar(jar)
        jar_string = json.dumps(jar_dict)

        self._set_user_key(self._username, 'cookies', jar_string)
