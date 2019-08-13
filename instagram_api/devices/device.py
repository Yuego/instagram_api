from distutils.version import LooseVersion

from .good import GoodDevices
from .interface import DeviceInterface
from .user_agent import UserAgent


class Device(DeviceInterface):

    REQUIRED_ANDROID_VERSION = '2.2'

    _app_version: str
    _version_code: str
    _user_locale: str
    _device_string: str
    _user_agent: str
    _fb_user_agents: dict
    _android_version: str
    _android_release: str
    _dpi: str
    _resolution: str
    _manufacturer: str
    _brand: str
    _model: str
    _device: str
    _cpu: str

    def __init__(self,
                 app_version: str,
                 version_code: str,
                 user_locale: str,
                 device_string: str = None,
                 auto_fallback: bool = True):

        self._app_version = app_version
        self._version_code = version_code
        self._user_locale = user_locale

        if auto_fallback and (device_string is None or not GoodDevices.is_good_device(device_string)):
            device_string = GoodDevices.get_random_good_device()

        self._init_from_device_string(device_string)

    def _init_from_device_string(self, device_string: str):
        assert isinstance(device_string, str) and device_string, 'Device string is empty'

        parts = [p.strip() for p in device_string.split('; ')]
        assert len(parts) == 7, f'Device string `{device_string}` does not conform to the required device format'

        android_os = parts[0].split('/', 1)
        assert (
            LooseVersion(android_os) > LooseVersion(self.REQUIRED_ANDROID_VERSION),
            f'Device string `{device_string}` does not meet the minimum required Android version '
            f'`{self.REQUIRED_ANDROID_VERSION}` for Instagram'
        )

        resolution = parts[2].split('x', 1)
        pixel_count = int(resolution[0]) * int(resolution[1])
        assert (
            pixel_count >= 2073600,
            f'Device string `{device_string}` does not meet the minimum resolution requirement of 1920x1080'
        )

        manufacturer_and_brand = parts[3].split('/', 1)

        self._device_string = device_string
        self._android_version = android_os[0]
        self._android_release = android_os[1]
        self._dpi = parts[1]
        self._resolution = parts[2]
        self._manufacturer = manufacturer_and_brand[0]
        self._brand = manufacturer_and_brand[1] if len(manufacturer_and_brand) > 1 else None
        self._model = parts[4]
        self._device = parts[5]
        self._cpu = parts[6]

        self._user_agent = UserAgent.build_user_agent(self._app_version, self._user_locale, self)

        self._fb_user_agents = {}

    def get_device_string(self):
        return self._device_string

    def get_android_version(self):
        return self._android_version

    def get_android_release(self):
        return self._android_release

    def get_dpi(self):
        return self._dpi

    def get_resolution(self):
        return self._resolution

    def get_manufacturer(self):
        return self._manufacturer

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_device(self):
        return self._device

    def get_cpu(self):
        return self._cpu

    def get_user_agent(self):
        return self._user_agent

    def get_fb_user_agent(self, app_name):
        if app_name not in self._fb_user_agents:
            self._fb_user_agents[app_name] = UserAgent.build_fb_user_agent(
                app_name,
                self._app_version,
                self._version_code,
                self._user_locale,
                self,
            )

        return self._fb_user_agents[app_name]
