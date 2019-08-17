from .mapper import ApiResponse, ApiResponseInterface

from .model import Surface, User

__all__ = ['BootstrapUserResponse']


class BootstrapUserResponseInterface(ApiResponseInterface):
    surfaces: [Surface]
    users: [User]


class BootstrapUserResponse(ApiResponse, BootstrapUserResponseInterface):
    pass
