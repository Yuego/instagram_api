from time import time

from instagram_api.property_mapper import PropertyMapperBase

from .rewrite_rule import RewriteRule

__all__ = ['Token']


class Token(PropertyMapperBase):
    DEFAULT_TTL = 3600

    JSON_PROPERTY_MAP = {
        'carrier_name': str,
        'carrier_id': int,
        'ttl': int,
        'features': None,
        'request_time': str,
        'token_hash': str,
        'rewrite_rules': [RewriteRule],
        'enabled_wallet_defs_keys': None,
        'deadline': str,
        'zero_cms_fetch_interval_seconds': int,
    }

    def expires_at(self):
        ttl = getattr(self, 'ttl', 0)
        if not ttl:
            ttl = self.DEFAULT_TTL

        return time() + ttl
