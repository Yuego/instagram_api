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
    def has_user(self, username: str) -> bool: ...

    @abstractmethod
    def move_user(self, old_username: str, new_username: str): ...

    @abstractmethod
    def delete_user(self, username: str): ...

    @abstractmethod
    def change_user(self, username: str): ...

    @abstractmethod
    def is_maybe_logged_in(self) -> bool: ...

    @abstractmethod
    def erase_device_settings(self): ...

    @abstractmethod
    def get(self, key: str, default=None): ...

    @abstractmethod
    def set(self, key: str, value): ...

    @abstractmethod
    def has_cookies(self): ...

    @abstractmethod
    def get_cookies(self) -> Optional[ClientCookieJar]: ...

    @abstractmethod
    def set_cookies(self, jar: ClientCookieJar): ...

    @abstractmethod
    def reset_cookies(self): ...

    @abstractmethod
    def set_rewrite_rules(self, rules: dict): ...

    @abstractmethod
    def get_rewrite_rules(self) -> dict: ...
