from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['ContextualFilters', 'ContextualFiltersInterface']


class ContextualFiltersInterface(ApiInterfaceBase):
    clause_type: str
    filters: AnyType
    clauses: AnyType


class ContextualFilters(PropertyMapper, ContextualFiltersInterface):
    pass
