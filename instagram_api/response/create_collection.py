from .mapper import ApiResponse
from .model.collection import CollectionInterface

__all__ = ['CreateCollectionResponse']


class CreateCollectionResponseInterface(CollectionInterface):
    pass


class CreateCollectionResponse(ApiResponse, CreateCollectionResponseInterface):
    pass
