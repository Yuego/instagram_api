from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = ['ConstraintsInterface']


class ConstraintsInterface(metaclass=ABCMeta):

    @abstractproperty
    def title(self) -> str: ...

    @abstractproperty
    def min_aspect_ratio(self) -> float: ...

    @abstractproperty
    def max_aspect_ratio(self) -> float: ...

    @abstractproperty
    def recommended_ratio(self) -> float: ...

    @abstractproperty
    def recommended_ratio_deviation(self) -> float: ...

    @abstractproperty
    def use_recommended_ratio_by_default(self) -> bool: ...

    @abstractproperty
    def min_duration(self) -> float: ...

    @abstractproperty
    def max_duration(self) -> float: ...
