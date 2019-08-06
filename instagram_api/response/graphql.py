from .base_response import Response
from .model import GraphData

__all__ = ['GraphQLResponse']


class GraphQLResponse(Response):
    JSON_PROPERTY_MAP = {
        'data': GraphData,
    }

    def is_ok(self):
        return True
