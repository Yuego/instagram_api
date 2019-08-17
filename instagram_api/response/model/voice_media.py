from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .direct_thread_item_media import DirectThreadItemMedia

__all__ = ['VoiceMedia', 'VoiceMediaInterface']


class VoiceMediaInterface(ApiInterfaceBase):
    media: DirectThreadItemMedia


class VoiceMedia(PropertyMapper, VoiceMediaInterface):
    pass
