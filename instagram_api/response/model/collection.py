from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .item import Item

__all__ = ['Collection', 'CollectionInterface']


class CollectionInterface(ApiInterfaceBase):
    collection_id: int
    collection_name: str
    cover_media: Item


class Collection(PropertyMapper, CollectionInterface):
    pass
