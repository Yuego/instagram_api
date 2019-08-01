from abc import ABCMeta, abstractmethod
from typing import Any

__all__ = ['ExperimentsInterface']


class ExperimentsInterface(metaclass=ABCMeta):

    @abstractmethod
    def is_experiment_enabled(self, experiment: str, param: str, default: bool = False) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_experiment_param(self, experiment: str, param: str, default: Any = None) -> Any:
        raise NotImplementedError
