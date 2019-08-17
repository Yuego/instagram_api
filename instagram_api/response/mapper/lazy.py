import importlib
import os

from importlib.util import find_spec

from .mapper_type import PropertyMapperType

MAPPER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))

__all__ = ['Lazy']


class lazy(type):

    def __getattr__(cls, name: str):
        _module, _class = name.replace('__', '.').rsplit('.', 1)

        full_module_path = f'instagram_api.response.{_module}'

        spec = find_spec(full_module_path)

        if spec is None:
            raise ImportError(f'Module `{name}` not found!')

        class _Lazy(PropertyMapperType):
            module = _module
            class_name = _class

            def __call__(self, value):
                module = importlib.import_module(self.module)
                module_class = getattr(module, self.class_name)
                return module_class(value)

        return _Lazy


class Lazy(metaclass=lazy):
    pass
