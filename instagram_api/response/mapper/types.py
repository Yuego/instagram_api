import importlib
from importlib.util import find_spec
from .mapper_type import PropertyMapperType
from .exceptions import WrongType
from .lazy import Lazy
from datetime import datetime

__all__ = [
    'Timestamp',
    'AnyType',
    'Lazy',
]


class TimestampType(type):

    def __new__(cls, *args, **kwargs):

        class _Timestamp(PropertyMapperType):
            def __call__(self, value):
                if value is not None:
                    return datetime.utcfromtimestamp
                else:
                    return None

        return _Timestamp


class Timestamp(metaclass=TimestampType):
    pass


class AnyTypeType(type):

    def __new__(cls, *args, **kwargs):
        class _AnyType(PropertyMapperType):
            def __call__(self, value):
                return value

        return _AnyType


class AnyType(metaclass=AnyTypeType):
    pass

