from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .comment import Comment

__all__ = ['PropertyMapperBase', 'PropertyMapperBaseInterface']


class LiveCommentInterface(ApiInterfaceBase):
    comment: Comment
    offset: AnyType
    event: AnyType


class LiveComment(PropertyMapper, LiveCommentInterface):
    pass
