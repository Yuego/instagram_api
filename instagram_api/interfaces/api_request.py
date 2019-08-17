from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Any, Dict

from .api_response import ApiResponseInterface

__all__ = ['ApiRequestInterface']


class ApiRequestInterface(metaclass=ABCMeta):

    @abstractmethod
    def use_version(self, version: int) -> 'ApiRequestInterface': ...

    @abstractmethod
    def use_default_headers(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def require_auth(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def sign_post(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def sign_get(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def multi_json_response(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def compress_body(self, flag: bool) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_params(self, **params: Dict[str, Any]) -> 'ApiRequestInterface': ...

    @abstractmethod
    def add_posts(self, **posts: Dict[str, Any]) -> 'ApiRequestInterface': ...

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
    def get_response(self, response_type: type(ApiResponseInterface)) -> ApiResponseInterface: ...
