from .mapper import ApiResponse
from .model.collection import CollectionInterface

__all__ = ['EditCollectionResponse']


class EditCollectionResponseInterface(CollectionInterface):
    pass


class EditCollectionResponse(ApiResponse, EditCollectionResponseInterface):
    pass
