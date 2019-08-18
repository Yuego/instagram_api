from typing import List

from time import time

from ..mapper import PropertyMapper, ApiInterfaceBase
from ..mapper.types import Timestamp, AnyType

from .rewrite_rule import RewriteRule

__all__ = ['Token', 'TokenInterface']


class TokenInterface(ApiInterfaceBase):
    carrier_name: str
    carrier_id: int
    ttl: int
    features: AnyType
    request_time: str
    token_hash: str
    rewrite_rules: [RewriteRule]
    enabled_wallet_defs_keys: AnyType
    deadline: str
    zero_cms_fetch_interval_seconds: int


class Token(PropertyMapper, TokenInterface):
    DEFAULT_TTL = 3600

    def expires_at(self):
        ttl = getattr(self, 'ttl', 0)
        if not ttl:
            ttl = self.DEFAULT_TTL

        return time() + ttl
