from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .param import Param

__all__ = ['Experiment', 'ExperimentInterface']


class ExperimentInterface(ApiInterfaceBase):
    name: str
    group: str
    additional_params: AnyType
    params: [Param]
    logging_id: int
    expired: bool


class Experiment(PropertyMapper, ExperimentInterface):
    pass
