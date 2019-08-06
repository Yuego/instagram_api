from instagram_api.property_mapper import PropertyMapperBase

from .param import Param

__all__ = ['Experiment']


class Experiment(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'name': str,
        'group': str,
        'additional_params': None,
        'params': [Param],
        'logging_id': int,
        'expired': bool,
    }
