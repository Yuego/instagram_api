from .mapper import ApiResponse, ApiResponseInterface

__all__ = ['DeleteCollectionResponse']


class DeleteCollectionResponseInterface(ApiResponseInterface):
    pass


class DeleteCollectionResponse(ApiResponse, DeleteCollectionResponseInterface):
    pass
