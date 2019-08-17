from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['AudioContext', 'AudioContextInterface']


class AudioContextInterface(ApiInterfaceBase):
    audio_src: str
    duration: int


class AudioContext(PropertyMapper, AudioContextInterface):
    pass
