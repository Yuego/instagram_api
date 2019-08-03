from instagram_api.property_mapper import PropertyMapperBase

from .qp_node import QPNode
from .time_range import TimeRange

__all__ = ['Edges']


class Edges(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'priority': int,
        'time_range': TimeRange,
        'node': QPNode,
    }
