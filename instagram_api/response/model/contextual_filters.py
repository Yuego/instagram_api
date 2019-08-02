from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['ContextualFilters']


class ContextualFilters(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'clause_type': str,
        'filters': None,
        'clauses': None,
    }
