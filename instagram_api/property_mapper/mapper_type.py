from abc import ABCMeta, abstractmethod

__all__ = ['PropertyMapperType']


class PropertyMapperType(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, value):
        raise NotImplementedError

