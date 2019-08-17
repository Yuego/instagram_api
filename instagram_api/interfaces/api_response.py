from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = ['ApiResponseInterface']


class ApiResponseInterface(metaclass=ABCMeta):

    @abstractproperty
    def is_ok(self): ...

    @abstractmethod
    def get_message(self): ...

    @abstractproperty
    def http_response(self): ...

    @abstractproperty
    def has_http_response(self): ...
