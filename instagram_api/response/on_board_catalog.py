from .base_response import Response

__all__ = ['OnBoardCatalogResponse']


class OnBoardCatalogResponse(Response):
    JSON_PROPERTY_MAP = {
        'shopping_onboarding_state': str,
        'current_catalog_id': str,
        'is_business_targeted_for_shopping': bool,
    }
