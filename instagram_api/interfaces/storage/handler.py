from abc import ABCMeta, abstractmethod
from typing import Optional

from instagram_api.utils.http import ClientCookieJar

__all__ = ['StorageHandlerInterface']


class StorageHandlerInterface(metaclass=ABCMeta):
    ON_CLOSE_USER = 'on_close_user'
    SUPPORTED_CALLBACKS = [
        ON_CLOSE_USER,
    ]

    @abstractmethod
    def has_user(self, username: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def move_user(self, old_username: str, new_username: str):
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, username: str):
        raise NotImplementedError

    @abstractmethod
    def select_user(self, username: str):
        raise NotImplementedError

    @abstractmethod
    def is_maybe_logged_in(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def erase_device_settings(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str, default=None):
        raise NotImplementedError

    @abstractmethod
    def set(self, key: str, value):
        raise NotImplementedError

    @abstractmethod
    def has_cookies(self):
        raise NotImplementedError

    @abstractmethod
    def get_cookies(self) -> Optional[ClientCookieJar]:
        raise NotImplementedError

    @abstractmethod
    def set_cookies(self, jar: ClientCookieJar):
        raise NotImplementedError

    @abstractmethod
    def reset_cookies(self):
        raise NotImplementedError

    @abstractmethod
    def set_rewrite_rules(self, rules: dict):
        raise NotImplementedError

    @abstractmethod
    def get_rewrite_rules(self) -> dict:
        raise NotImplementedError
