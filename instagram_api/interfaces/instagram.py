from abc import ABCMeta, abstractmethod

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

    account: ApiRequestInterface
    business: ApiRequestInterface
    collection: ApiRequestInterface
    creative: ApiRequestInterface
    direct: ApiRequestInterface
    discover: ApiRequestInterface
    hashtag: ApiRequestInterface
    highlight: ApiRequestInterface
    tv: ApiRequestInterface
    internal: ApiRequestInterface
    live: ApiRequestInterface
    location: ApiRequestInterface
    media: ApiRequestInterface
    people: ApiRequestInterface
    push: ApiRequestInterface
    shopping: ApiRequestInterface
    story: ApiRequestInterface
    timeline: ApiRequestInterface
    usertag: ApiRequestInterface
