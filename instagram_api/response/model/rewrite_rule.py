from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

__all__ = ['RewriteRule', 'RewriteRuleInterface']


class RewriteRuleInterface(ApiInterfaceBase):
    matcher: str
    replacer: str


class RewriteRule(PropertyMapper, RewriteRuleInterface):
    pass
