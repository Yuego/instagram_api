from abc import ABCMeta, abstractmethod

from .client import ClientInterface
from .device import DeviceInterface
from .request import RequestInterface
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

    experiments: list

    client: ClientInterface

    device: DeviceInterface
    settings: StorageHandlerInterface

    account: RequestInterface
    business: RequestInterface
    collection: RequestInterface
    creative: RequestInterface
    direct: RequestInterface
    discover: RequestInterface
    hashtag: RequestInterface
    highlight: RequestInterface
    tv: RequestInterface
    internal: RequestInterface
    live: RequestInterface
    location: RequestInterface
    media: RequestInterface
    people: RequestInterface
    push: RequestInterface
    shopping: RequestInterface
    story: RequestInterface
    timeline: RequestInterface
    usertag: RequestInterface
