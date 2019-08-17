from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Effect', 'EffectInterface']


class EffectInterface(ApiInterfaceBase):
    title: str
    id: int
    effect_id: int
    effect_file_id: int
    asset_url: str
    thumbnail_url: str
    instructions: AnyType


class Effect(PropertyMapper, EffectInterface):
    pass
