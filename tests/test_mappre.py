from instagram_api.response.mapper.mapper_type import PropertyMapperType
from instagram_api.response.mapper.types import Timestamp, Lazy, AnyType


def test_mapper():
    pmt = PropertyMapperType
    pmtt = Timestamp
    pmtl = Lazy
    pmta = AnyType

    ll = list
    li = int

    t = issubclass(Timestamp, PropertyMapperType)

    l = issubclass(Lazy, PropertyMapperType)

    a = issubclass(AnyType, PropertyMapperType)

    z = 'some'
