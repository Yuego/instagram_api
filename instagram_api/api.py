
from .constants import Constants


class ApiMeta(type):

    def __new__(cls, name, bases, attrs):

        new_class = super().__new__(cls, name, bases, attrs)

        for version, url in Constants.API_URLS.items():
            def get_method(url):

                @property
                def method(self):
                    self.url = url
                    return self

                return method

            setattr(new_class, f'v{version}', get_method(url))

        return new_class


class InstagramApi(metaclass=ApiMeta):

    url: str
