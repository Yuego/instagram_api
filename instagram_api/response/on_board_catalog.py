from .base_response import ApiResponse

__all__ = ['OnBoardCatalogResponse']


class OnBoardCatalogResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'shopping_onboarding_state': str,
        'current_catalog_id': str,
        'is_business_targeted_for_shopping': bool,
    }
