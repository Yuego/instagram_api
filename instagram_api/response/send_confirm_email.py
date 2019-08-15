from .base_response import ApiResponse

__all__ = ['SendConfirmEmailResponse']


class SendConfirmEmailResponse(ApiResponse):
    JSON_PROPERTY_MAP = {
        'title': None,
        'is_email_legit': None,
        'body': None,
    }
