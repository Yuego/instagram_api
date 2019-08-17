from abc import ABCMeta, abstractmethod, abstractstaticmethod, abstractproperty
from typing import Union, Any

from requests import Response

from .api_response import ApiResponseInterface

__all__ = ['ClientInterface']


class ClientInterface(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, endpoint: str, headers: dict = None, data: dict = None, files: dict = None) -> Response: ...

    @abstractmethod
    def set_proxy(self, proxy: Union[str, list, dict]): ...

    @abstractmethod
    def clear_proxy(self): ...

    @abstractmethod
    def update_from_current_settings(self, reset_cookie_jar: bool = False): ...

    @abstractmethod
    def load_cookie_jar(self, reset_cookie_jar: bool = False): ...

    @abstractmethod
    def save_cookie_jar(self): ...

    @abstractmethod
    def get_cookie(self, name: str, domain: str = None, path: str = None) -> Any: ...

    @abstractmethod
    def get_token(self): ...

    @abstractmethod
    def map_server_response(self,
                            api_response: type(ApiResponseInterface),
                            json_response: str,
                            http_response: Response,
                            ) -> ApiResponseInterface: ...

    @abstractstaticmethod
    def api_body_decode(json_string: str) -> dict: ...

    @abstractproperty
    def zero_rating(self): ...

    @abstractproperty
    def fake_cookies(self): ...
