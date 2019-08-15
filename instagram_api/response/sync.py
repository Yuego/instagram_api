from .base_response import ApiResponse
from .model import Experiment

__all__ = ['SyncResponse']


class SyncResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'experiments': Experiment,
    }
