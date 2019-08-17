
from .mapper_meta import PropertyMapperMeta
from .mapper_base import PropertyMapperBase


class PropertyMapper(PropertyMapperBase, metaclass=PropertyMapperMeta):
    pass
