from ..mapper import PropertyMapper, ApiInterfaceBase

from .text import Text

__all__ = ['Action', 'ActionInterface']


class ActionInterface(ApiInterfaceBase):
    title: Text
    url: str
    limit: int
    dismiss_promotion: bool


class Action(PropertyMapper, ActionInterface):
    pass
