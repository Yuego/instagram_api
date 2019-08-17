from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AssetModel', 'AssetModelInterface']


class AssetModelInterface(ApiInterfaceBase):
    asset_url: str
    id: int


class AssetModel(PropertyMapper, AssetModelInterface):
    pass
