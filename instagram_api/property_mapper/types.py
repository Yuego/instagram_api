from .mapper_type import PropertyMapperType

from datetime import datetime

__all__ = [
    'timestamp',
    'Integer',
    'Float',
    'String',
    'Bool',
    'Timestamp',
]


def timestamp(timestamp: int):
    if timestamp:
        return datetime.utcfromtimestamp(timestamp)
    else:
        return None


class IntegerType(PropertyMapperType):

    def __call__(self, value):
        if value is None:
            return None
        else:
            return int(value)


Integer = IntegerType()


class FloatType(PropertyMapperType):

    def __call__(self, value):
        if value is None:
            return None
        else:
            return float(value)


Float = FloatType()


class StringType(PropertyMapperType):

    def __call__(self, value):
        if value is None:
            return None
        else:
            return str(value)


String = StringType()


class BooleanType(PropertyMapperType):

    def __call__(self, value):
        if value is None:
            return None
        else:
            return bool(value)


Bool = BooleanType()


class TimestampType(PropertyMapperType):

    def __call__(self, value: int):
        if value:
            return datetime.utcfromtimestamp(value)

        else:
            return None


Timestamp = TimestampType()
