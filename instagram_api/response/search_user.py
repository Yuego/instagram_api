from .base_response import ApiResponse
from .model import User

__all__ = ['SearchUserResponse']


class SearchUserResponse(ApiResponse):
    JSON_PROPERTY_MAP = dict(
        has_more=bool,
        num_results=int,
        rank_token=str,
        users=[User],
    )
