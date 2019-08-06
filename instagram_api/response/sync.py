from .base_response import Response
from .model import Experiment

__all__ = ['SyncResponse']


class SyncResponse(Response):
    JSON_PROPERTY_MAP = {
        'experiments': Experiment,
    }
