from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Optional

__all__ = ['DeviceInterface']


class DeviceInterface(metaclass=ABCMeta):

    @abstractproperty
    def device_string(self) -> str: ...

    @abstractproperty
    def user_agent(self) -> str: ...

    @abstractproperty
    def android_version(self) -> str: ...

    @abstractproperty
    def android_release(self) -> str: ...

    @abstractproperty
    def dpi(self) -> str: ...

    @abstractproperty
    def resolution(self) -> str: ...

    @abstractproperty
    def manufacturer(self) -> str: ...

    @abstractproperty
    def brand(self) -> Optional[str]: ...

    @abstractproperty
    def model(self) -> str: ...

    @abstractproperty
    def device(self): ...

    @abstractproperty
    def cpu(self) -> str: ...

    @abstractmethod
    def get_fb_user_agent(self, app_name: str) -> str: ...
