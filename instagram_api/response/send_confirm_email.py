from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['SendConfirmEmailResponse']


class SendConfirmEmailResponseInterface(ApiResponseInterface):
    title: AnyType
    is_email_legit: AnyType
    body: AnyType


class SendConfirmEmailResponse(ApiResponse, SendConfirmEmailResponseInterface):
    pass
