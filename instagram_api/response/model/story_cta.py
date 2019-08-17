from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .android_links import AndroidLinks

__all__ = ['StoryCta', 'StoryCtaInterface']


class StoryCtaInterface(ApiInterfaceBase):
    links: [AndroidLinks]
    felix_deep_link: str


class StoryCta(PropertyMapper, StoryCtaInterface):
    pass
