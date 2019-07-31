from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['AccountSummaryUnit']


class AccountSummaryUnit(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'posts_count': int,
    }
