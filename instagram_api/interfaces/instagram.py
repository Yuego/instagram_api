from abc import ABCMeta, abstractmethod
from typing import Any, Optional, Union

from instagram_api import request, response

from .client import ClientInterface
from .device import DeviceInterface
from .api_request import ApiRequestInterface
from .storage import StorageHandlerInterface

__all__ = ['InstagramInterface']


class InstagramInterface(metaclass=ABCMeta):
    EXPERIMENTS_REFRESH = 7200

    username: str
    password: str

    debug: bool
    debug_truncate: bool
    debug_developer: bool = False

    uuid: str
    advertising_id: str
    device_id: str
    phone_id: str
    account_id: int

    is_maybe_logged_in: bool = False

    session_id: str

    experiments: dict

    client: ClientInterface

    device: DeviceInterface
    settings: StorageHandlerInterface

    account: request.Account
    business: request.Business
    collection: request.Collection
    creative: request.Creative
    direct: request.Direct
    discover: request.Discover
    hashtag: request.Hashtag
    highlight: request.Highlight
    tv: request.Tv
    internal: request.Internal
    live: request.Live
    location: request.Location
    media: request.Media
    people: request.People
    push: request.Push
    shopping: request.Shopping
    story: request.Story
    timeline: request.Timeline
    usertag: request.Usertag

    @abstractmethod
    def set_verify_ssl(self, state: Union[bool, str]): ...

    @abstractmethod
    def get_verify_ssl(self) -> Union[bool, str]: ...

    @abstractmethod
    def set_proxy(self, proxy: Optional[Union[str, dict, list]]): ...

    @abstractmethod
    def get_proxy(self) -> Optional[Union[str, dict, list]]: ...

    @abstractmethod
    def login(self,
              username: str,
              password: str,
              app_refresh_interval: int = 1800) -> Optional[response.LoginResponse]: ...

    # TODO: указать возвращаемый тип
    @abstractmethod
    def finish_two_factor_login(self,
                                username: str,
                                password: str,
                                two_factor_identifier: str,
                                verification_code: str,
                                verification_method: int,
                                app_refresh_interval: int = 1800,
                                username_handler: str = None) -> response.LoginResponse: ...

    # TODO: указать возвращаемый тип
    @abstractmethod
    def send_two_factor_login_sms(self,
                                  username: str,
                                  password: str,
                                  two_factor_identifier: str,
                                  username_handler: str = None) -> response.TwoFactorLoginSMSResponse: ...

    # TODO: указать возвращаемый тип
    def user_lookup(self, username: str) -> response.UsersLookupResponse: ...

    # TODO: указать возвращаемый тип
    def send_recovery_email(self, username: str) -> response.RecoveryResponse: ...

    # TODO: указать возвращаемый тип
    def send_recovery_sms(self, username: str) -> response.RecoveryResponse: ...

    # TODO: указать возвращаемый тип
    def logout(self) -> response.LogoutResponse: ...

    def get_experiment_param(self, experiment: str, param: str, default: str = None) -> Any: ...

    def request(self, url: str) -> ApiRequestInterface: ...
