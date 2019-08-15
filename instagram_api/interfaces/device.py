from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Optional

__all__ = ['DeviceInterface']


class DeviceInterface(metaclass=ABCMeta):

    @abstractproperty
    def device_string(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def user_agent(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def android_version(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def android_release(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def dpi(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def resolution(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def manufacturer(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def brand(self) -> Optional[str]:
        raise NotImplementedError

    @abstractproperty
    def model(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def device(self):
        raise NotImplementedError

    @abstractproperty
    def cpu(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_fb_user_agent(self, app_name: str) -> str:
        raise NotImplementedError
