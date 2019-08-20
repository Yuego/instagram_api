from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Any, Dict, TypeVar, Type

T = TypeVar('T')


__all__ = ['ApiRequestInterface']


class ApiRequestInterface(metaclass=ABCMeta):

    @abstractmethod
    def set_version(self, version: int) -> 'ApiRequestInterface': ...

    @abstractmethod
    def set_add_default_headers(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def set_needs_auth(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def set_signed_post(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def set_signed_get(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def set_is_multi_response(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def set_is_body_compressed(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_params(self, **params: Dict[str, Any]) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_posts(self,
                  _uid: str = None,
                  _uuid: str = None,
                  _csrftoken: str = None,
                  phone_id: str = None,
                  device_id: str = None,
                  adid: str = None,
                  **posts: Dict[str, Any]) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_unsigned_posts(self, **posts: Dict[str, Any]) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_file(self, key: str, path: str, name: str, headers: Dict[str, str] = None) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_file_data(self,
                      key: str,
                      data: str,
                      name: str,
                      headers: Dict[str, str] = None) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_headers(self, **headers: Dict[str, str]) -> 'ApiRequestInterface': ...

    @abstractmethod
    def get_response(self, response_type: Type[T]) -> T: ...
