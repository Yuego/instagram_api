from instagram_api import response
from .base import CollectionBase

__all__ = ['Shopping']


class Shopping(CollectionBase):

    def get_on_tag_product_info(self,
                                product_id: int,
                                media_id: int,
                                merchant_id: int,
                                device_width: int = 720) -> response.OnTagProductResponse: ...

    def get_catalogs(self, locale: str = 'en_US') -> response.GraphQLResponse: ...

    def get_catalog_items(self, catalog_id: int, query: str = '', offset: int = None) -> response.GraphQLResponse: ...

    def set_on_board_catalog(self, catalog_id: int) -> response.OnBoardCatalogResponse: ...
