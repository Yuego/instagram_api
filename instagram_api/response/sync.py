from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import Experiment

__all__ = ['SyncResponse']


class SyncResponseInterface(ApiResponseInterface):
    experiments: Experiment


class SyncResponse(ApiResponse, SyncResponseInterface):
    pass
