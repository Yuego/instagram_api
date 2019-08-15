

class PropertyMapperException(Exception):
    pass


class UnsupportedType(PropertyMapperException):
    pass


class WrongType(PropertyMapperException):
    pass
