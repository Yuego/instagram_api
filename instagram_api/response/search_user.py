
from instagram_api.property_mapper import PropertyMapper

from .model import User

__all__ = ['SearchUserResponse']


class SearchUserResponse(PropertyMapper):

    JSON_PROPERTY_MAP = dict(
        has_more=bool,
        num_results=int,
        rank_token=str,
        users=[User],
    )
