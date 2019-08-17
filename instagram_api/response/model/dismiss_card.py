from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['DismissCard', 'DismissCardInterface']


class DismissCardInterface(ApiInterfaceBase):
    card_id: int
    image_url: str
    title: AnyType
    message: AnyType
    button_text: AnyType
    camera_target: AnyType
    face_filter_id: AnyType


class DismissCard(PropertyMapper, DismissCardInterface):
    pass
