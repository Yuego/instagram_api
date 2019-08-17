from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Explore', 'ExploreInterface']


class ExploreInterface(ApiInterfaceBase):
    explanation: AnyType
    actor_id: int
    source_token: AnyType


class Explore(PropertyMapper, ExploreInterface):
    pass
