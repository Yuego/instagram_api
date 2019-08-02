from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['CommentTranslations']


class CommentTranslations(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': int,
        'translation': None,
    }
