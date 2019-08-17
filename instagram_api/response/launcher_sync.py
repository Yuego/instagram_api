from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['LauncherSyncResponse']


class LauncherSyncResponseInterface(ApiResponseInterface):
    configs: AnyType


class LauncherSyncResponse(ApiResponse, LauncherSyncResponseInterface):
    pass
