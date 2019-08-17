from urllib3.response import HTTPResponse

from instagram_api.property_mapper import PropertyMapper

from .model import UnknownMessage


class ApiResponse(PropertyMapper):


        _message: [UnknownMessage]
