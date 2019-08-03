from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['FormerUsernameInfo']


class FormerUsernameInfo(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'has_former_usernames': bool,
    }
