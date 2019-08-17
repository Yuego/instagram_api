from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType
from .model import GraphData

__all__ = ['GraphQLResponse']


class GraphQLResponseInterface(ApiResponseInterface):
    data: GraphData


class GraphQLResponse(ApiResponse, GraphQLResponseInterface):

    def is_ok(self):
        return True
