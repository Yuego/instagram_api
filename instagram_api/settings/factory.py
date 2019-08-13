import importlib

from instagram_api.exceptions.settings import SettingsException

from .storage.interface import StorageInterface
from .handler import StorageHandler
"""

STORAGE = 'instagram_api.settings.storage.redis.RedisStorage

"""


class StorageFactory:


    @staticmethod
    def create_handler(storage: str, storage_config: dict, callbacks: list = None):
        callbacks = callbacks or []

        try:
            module_name, class_name = storage.rsplit('.', 1)

            storage_module = importlib.import_module(module_name)
            storage_class = getattr(storage_module, class_name)
        except ImportError:
            raise SettingsException(f'Can not import storage module `{storage}`', response={})
        except AttributeError:
            raise SettingsException(f'Can`t load storage module `{storage}`', response={})

        if not issubclass(storage_class, StorageInterface):
            raise SettingsException(f'Storage class must inherit StorageInterface interface', response={})

        storage = storage_class()

        return StorageHandler(storage, storage_config, callbacks)



