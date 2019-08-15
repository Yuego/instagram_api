from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = ['ApiResponseInterface']


class ApiResponseInterface(metaclass=ABCMeta):

    @abstractproperty
    def is_ok(self):
        raise NotImplementedError

    @abstractmethod
    def get_message(self):
        raise NotImplementedError

    @abstractproperty
    def http_response(self):
        raise NotImplementedError

    @abstractproperty
    def has_http_response(self):
        raise NotImplementedError
