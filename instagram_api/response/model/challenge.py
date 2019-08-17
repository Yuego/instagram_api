from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['Challenge', 'ChallengeInterface']


class ChallengeInterface(ApiInterfaceBase):
    url: str
    api_path: AnyType
    hide_webview_header: AnyType
    lock: AnyType
    logout: AnyType
    native_flow: AnyType


class Challenge(PropertyMapper, ChallengeInterface):
    pass
