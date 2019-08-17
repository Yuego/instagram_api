from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AdsInfo', 'AdsInfoInterface']


class AdsInfoInterface(ApiInterfaceBase):
    has_ads: bool
    ads_url: str


class AdsInfo(PropertyMapper, AdsInfoInterface):
    pass
