from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .contextual_filters import ContextualFilters
from .creative import Creative
from .template import Template

__all__ = ['QPNode', 'QPNodeInterface']


class QPNodeInterface(ApiInterfaceBase):
    id: int
    promotion_id: int
    max_impressions: int
    triggers: [str]
    contextual_filters: ContextualFilters
    template: Template
    creatives: [Creative]


class QPNode(PropertyMapper, QPNodeInterface):
    pass
