
from instagram_api.exceptions.settings import SettingsException
from .interface import StorageInterface

__all__ = ['StorageBase']

_default_prefix = '_ig'


class StorageBase(StorageInterface):

    _prefix: str = _default_prefix
    _username: str = None

    def open(self, config: dict):
        prefix = config.pop('prefix', _default_prefix) or _default_prefix
        self._prefix = prefix or _default_prefix

    def _user_key(self, username: str, key: str):
        return f'{self._prefix}{username}_{key}'

    def _get_user_key(self, username: str, key: str):
        raise NotImplementedError

    def _set_user_key(self, username: str, key: str, value):
        raise NotImplementedError

    def _del_user_key(self, username: str, key: str):
        raise NotImplementedError

    def open_user(self, username: str):
        self._username = username

    def close_user(self):
        self._username = None

    def move_user(self, old_username: str, new_username: str):
        if not self.has_user(old_username):
            raise SettingsException(f'Cannot move non-existent user {old_username}', response={})

        if self.has_user(new_username):
            raise SettingsException(f'Refusing to owerwrite existing user data {new_username}', response={})

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

    def load_user_cookies(self):
        return self._get_user_key(self._username, 'cookies')

    def save_user_cookies(self, data: dict):
        self._set_user_key(self._username, 'cookies', data)
