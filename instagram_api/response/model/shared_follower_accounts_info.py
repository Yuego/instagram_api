from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['SharedFollowerAccountsInfo']


class SharedFollowerAccountsInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'has_shared_follower_accounts': bool,
    }
