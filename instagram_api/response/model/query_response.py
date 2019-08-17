from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .shadow_instagram_user import ShadowInstagramUser

__all__ = ['QueryResponse', 'QueryResponseInterface']


class QueryResponseInterface(ApiInterfaceBase):
    shadow_instagram_user: ShadowInstagramUser


class QueryResponse(PropertyMapper, QueryResponseInterface):
    pass
