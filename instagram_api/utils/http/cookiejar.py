import pickle
import threading
from http.cookiejar import CookiePolicy
from requests.cookies import RequestsCookieJar
from typing import Union

__all__ = ['ClientCookieJar', 'create_cookie_jar_proxy']


class ClientCookieJar(RequestsCookieJar):

    def __init__(self, cookie_string: Union[str, bytes] = None, policy: CookiePolicy = None):
        super(ClientCookieJar, self).__init__(policy=policy)

        if cookie_string:
            if isinstance(cookie_string, bytes):
                self._cookies = pickle.loads(cookie_string)
            else:
                self._cookies = pickle.loads(cookie_string.encode('utf-8'))

    @property
    def auth_expires(self):
        for cookie in self:
            if cookie.name in ('ds_user_id', 'ds_user'):
                return cookie.expires

        return None

    def __getstate__(self):
        state = self.__dict__.copy()

        del state['_cookies_lock']

        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

        self._cookies_lock = threading.RLock()


def create_cookie_jar_proxy(obj, attr):
    """
    Создаём прокси-объект для того, чтоб везде не менять ссылку на CookiesJar
    по два раза.
    :param obj:
    :param attr:
    :return: CookieJarProxy
    """
    
    class CookieJarProxy(ClientCookieJar):
        jar = getattr(obj, attr)
            
        def __setattr__(self, key, value):
            setattr(self.jar, key, value)

        def __getattr__(self, item):
            return getattr(self.jar, item)

        def __contains__(self, item):
            return self.jar.__contains__(item)

        def __getitem__(self, item):
            return self.jar.__getitem__(item)

        def __setitem__(self, key, value):
            self.jar.__setitem__(key, value)

        def __delitem__(self, key):
            self.jar.__delitem__(key)

        def __iter__(self):
            return self.jar.__iter__()

        def __len__(self):
            return self.jar.__len__()

        def __repr__(self):
            return self.jar.__repr__()

        def __str__(self):
            return self.jar.__str__()

    return CookieJarProxy()
