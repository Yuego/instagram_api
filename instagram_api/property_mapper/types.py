import importlib
from importlib.util import find_spec

from .exceptions import WrongType
from .mapper_type import PropertyMapperType

from datetime import datetime

__all__ = [
    'timestamp',
    'LazyType',
    'Timestamp',
]


def timestamp(timestamp: int):
    if timestamp:
        return datetime.utcfromtimestamp(timestamp)
    else:
        return None


class LazyType(PropertyMapperType):
    path: str

    def __init__(self, module_name: str):
        module_path, class_name = module_name.rsplit('.', 1)
        full_module_path = f'instagram_api.response.{module_path}'
        spec = find_spec(full_module_path)
        if spec is None:
            raise WrongType(f'Module `{module_name} not found')
        else:
            self.path = '.'.join([full_module_path, class_name])

    def __call__(self, value):
        module = importlib.import_module(self.path)
        return module(value)


class TimestampType(PropertyMapperType):

    def __call__(self, value: int):
        if value:
            return datetime.utcfromtimestamp(value)

        else:
            return None


Timestamp = TimestampType()
