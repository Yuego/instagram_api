from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['OnBoardCatalogResponse']


class OnBoardCatalogResponseInterface(ApiResponseInterface):
    shopping_onboarding_state: str
    current_catalog_id: str
    is_business_targeted_for_shopping: bool


class OnBoardCatalogResponse(ApiResponse, OnBoardCatalogResponseInterface):
    pass
