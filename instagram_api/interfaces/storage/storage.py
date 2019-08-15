from abc import ABCMeta, abstractmethod

from instagram_api.utils.http import ClientCookieJar

__all__ = ['StorageInterface']


class StorageInterface(metaclass=ABCMeta):
    cookie_jar_class: type(ClientCookieJar)

    @abstractmethod
    def open(self, config: dict):
        raise NotImplementedError

    @abstractmethod
    def has_user(self, usenrame: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def open_user(self, username: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def move_user(self, old_username: str, new_username: str):
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, username: str):
        raise NotImplementedError

    @abstractmethod
    def load_user_settings(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def save_user_settings(self, settings: dict, trigger_key: str = None):
        raise NotImplementedError

    @abstractmethod
    def has_user_cookies(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def load_user_cookies(self) -> ClientCookieJar:
        raise NotImplementedError

    @abstractmethod
    def save_user_cookies(self, jar: ClientCookieJar):
        raise NotImplementedError

    @abstractmethod
    def close_user(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError

    def __del__(self):
        self.close()
