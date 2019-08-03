from instagram_api.property_mapper import PropertyMapperBase

__all__ = ['CatalogNode']


class CatalogNode(PropertyMapperBase):
    JSON_PROPERTY_MAP = {
        'id': str,
        'full_price': None,
        'current_price': None,
        'name': str,
        'description': str,
        'main_image_with_safe_fallback': None,
        'retailer_id': str,
    }
