from instagram_api.property_mapper import PropertyMapperBase

from .shadow_instagram_user import ShadowInstagramUser

__all__ = ['QueryResponse']


class QueryResponse(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'shadow_instagram_user': ShadowInstagramUser,
    }
