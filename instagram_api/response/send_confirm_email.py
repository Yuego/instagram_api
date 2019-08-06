from .base_response import Response

__all__ = ['SendConfirmEmailResponse']


class SendConfirmEmailResponse(Response):
    JSON_PROPERTY_MAP = {
        'title': None,
        'is_email_legit': None,
        'body': None,
    }
