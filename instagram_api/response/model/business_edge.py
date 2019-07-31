from instagram_api.property_mapper import PropertyMapperBase

from .business_node import BusinessNode

__all__ = ['BusinessEdge']


class BusinessEdge(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'node': BusinessNode,
        'cursor': None
    }
