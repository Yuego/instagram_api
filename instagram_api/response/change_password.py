from .mapper import ApiResponse, ApiResponseInterface

__all__ = ['ChangePasswordResponse']


class ChangePasswordResponseInterface(ApiResponseInterface):
    pass


class ChangePasswordResponse(ApiResponse, ChangePasswordResponseInterface):
    pass
