from .base_response import ApiResponse
from .model import GraphData

__all__ = ['GraphQLResponse']


class GraphQLResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'data': GraphData,
    }

    def is_ok(self):
        return True
