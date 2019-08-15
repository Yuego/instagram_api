from abc import ABCMeta, abstractmethod, abstractproperty

from .response import ApiResponseInterface

__all__ = ['RequestInterface']


class RequestInterface(metaclass=ABCMeta):

    @abstractmethod
    def use_version(self, version: int) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def use_default_headers(self, flag: bool) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def use_body(self, body) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def require_auth(self, flag: bool) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def sign_post(self, flag: bool) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def sign_get(self, flag: bool) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def join_response(self, flag: bool) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def compress_body(self, flag: bool) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def add_params(self, **params) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def add_posts(self, **posts) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def add_unsigned_posts(self, **posts) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def add_file(self, key: str, path: str, name: str, headers: dict = None) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def add_file_data(self, key: str, data: str, name: str, headers: dict = None) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def add_headers(self, **headers: dict) -> 'RequestInterface':
        raise NotImplementedError

    @abstractmethod
    def get_response(self, response_type: type(ApiResponseInterface)) -> ApiResponseInterface:
        raise NotImplementedError
