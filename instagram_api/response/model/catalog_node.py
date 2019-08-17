from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['CatalogNode', 'CatalogNodeInterface']


class CatalogNodeInterface(ApiInterfaceBase):
    id: str
    full_price: AnyType
    current_price: AnyType
    name: str
    description: str
    main_image_with_safe_fallback: AnyType
    retailer_id: int


class CatalogNode(PropertyMapper, CatalogNodeInterface):
    pass
