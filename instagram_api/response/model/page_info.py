from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['PageInfo', 'PageInfoInterface']


class PageInfoInterface(ApiInterfaceBase):
    end_cursor: str
    has_next_page: bool
    has_previous_page: bool


class PageInfo(PropertyMapper, PageInfoInterface):
    pass
