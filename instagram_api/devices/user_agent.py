from instagram_api.constants import Constants

from .good import GoodDevices
from .interface import DeviceInterface

__all__ = ['UserAgent']


fb_translate_table = str.maketrans('/;', '--')


class UserAgent:
    USER_AGENT_FORMAT = 'Instagram %s Android (%s/%s; %s; %s; %s; %s; %s; %s; %s; %s)'

    @staticmethod
    def build_user_agent(app_version: str, user_locale: str, device: DeviceInterface):
        manufacturer_with_brand = device.manufacturer
        if device.brand is not None:
            manufacturer_with_brand = f'{manufacturer_with_brand}/{device.brand}'

        return UserAgent.USER_AGENT_FORMAT % (
            app_version,
            device.android_version,
            device.android_release,
            device.dpi,
            device.resolution,
            manufacturer_with_brand,
            device.model,
            device.device,
            device.cpu,
            user_locale,
            Constants.VERSOIN_CODE,
        )

    @staticmethod
    def _escape_fb_string(string: str) -> str:
        res = []
        for char in string:
            if char == '&':
                res.append('&amp;')
            elif char < ' ' or char > '~':
                res.append(f'&#{ord(char)};')
            else:
                res.append(char)

        result = ''.join(res)
        result = result.translate(fb_translate_table)

        return result

    @staticmethod
    def build_fb_user_agent(app_name: str,
                            app_version: str,
                            version_code: str,
                            user_locale: str,
                            device: DeviceInterface):
        width, height = device.resolution.split('x')
        density = round(int(device.dpi.lower().replace('dpi', '')) / 160, 1)

        result = {
            'FBAN': app_name,
            'FBAV': app_version,
            'FBBV': version_code,
            'FBDM': '{density=%.1f,width=%d,height=%d}' % (density, width, height),
            'FBLC': user_locale,
            'FBCR': '',
            'FBMF': UserAgent._escape_fb_string(device.manufacturer),
            'FBBD': UserAgent._escape_fb_string(device.brand if device.brand else device.manufacturer),
            'FBPN': Constants.PACKAGE_NAME,
            'FBDV': UserAgent._escape_fb_string(device.model),
            'FBSV': UserAgent._escape_fb_string(device.android_release),
            'FBLR': 0,
            'FBBK': 1,
            'FBCA': UserAgent._escape_fb_string(GoodDevices.CPU_ABI),
        }

        return ''.join([
            '[',
            ';'.join([f'{key}/{value}' for key, value in result.items()]),
            ';]',
        ])
