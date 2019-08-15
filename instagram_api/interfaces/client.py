from abc import ABCMeta, abstractmethod, abstractstaticmethod
from typing import Union, Any

from requests import Response

from .response import ApiResponseInterface

__all__ = ['ClientInterface']


class ClientInterface(metaclass=ABCMeta):

    @abstractmethod
    def set_proxy(self, proxy: Union[str, list, dict]):
        raise NotImplementedError

    @abstractmethod
    def clear_proxy(self):
        raise NotImplementedError

    @abstractmethod
    def update_from_current_settings(self, reset_cookie_jar: bool = False):
        raise NotImplementedError

    @abstractmethod
    def load_cookie_jar(self, reset_cookie_jar: bool = False):
        raise NotImplementedError

    @abstractmethod
    def save_cookie_jar(self):
        raise NotImplementedError

    @abstractmethod
    def get_cookie(self, name: str, domain: str = None, path: str = None) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_token(self):
        raise NotImplementedError

    @abstractmethod
    def map_server_response(self,
                            api_response: type(ApiResponseInterface),
                            json_response: str,
                            http_response: Response,
                            ) -> ApiResponseInterface:
        raise NotImplementedError

    @abstractstaticmethod
    def api_body_decode(json_string: str) -> dict:
        raise NotImplementedError
