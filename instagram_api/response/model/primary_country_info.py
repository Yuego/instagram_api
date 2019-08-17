from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['PrimaryCountryInfo', 'PrimaryCountryInfoInterface']


class PrimaryCountryInfoInterface(ApiInterfaceBase):
    is_visible: bool
    has_country: bool
    country_name: str


class PrimaryCountryInfo(PropertyMapper, PrimaryCountryInfoInterface):
    pass
