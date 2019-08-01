from abc import ABCMeta, abstractmethod


class DeviceInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_device_string(self) -> str:
        raise NotImplementedError

    @property
    def device_string(self) -> str:
        return self.get_device_string()

    @abstractmethod
    def get_user_agent(self) -> str:
        raise NotImplementedError

    @property
    def user_agent(self) -> str:
        return self.get_user_agent()

    @abstractmethod
    def get_fb_user_agent(self) -> str:
        raise NotImplementedError

    @property
    def fb_user_agent(self) -> str:
        return self.get_user_agent()

    @abstractmethod
    def get_android_version(self) -> str:
        raise NotImplementedError

    @property
    def android_version(self) -> str:
        return self.get_android_version()

    @abstractmethod
    def get_android_release(self) -> str:
        raise NotImplementedError

    @property
    def android_release(self) -> str:
        return self.get_android_release()

    @abstractmethod
    def get_dpi(self) -> str:
        raise NotImplementedError

    @property
    def dpi(self) -> str:
        return self.get_dpi()

    @abstractmethod
    def get_resolution(self) -> str:
        raise NotImplementedError

    @property
    def resolution(self) -> str:
        return self.get_resolution()

    @abstractmethod
    def get_brand(self) -> str or None:
        raise NotImplementedError

    @property
    def brand(self) -> str or None:
        return self.get_brand()

    @abstractmethod
    def get_model(self) -> str:
        raise NotImplementedError

    @property
    def model(self) -> str:
        return self.get_model()

    @abstractmethod
    def get_cpu(self) -> str:
        raise NotImplementedError

    @property
    def cpu(self) -> str:
        return self.get_cpu()

