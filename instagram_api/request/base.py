from typing import Dict, List

import json

from instagram_api.interfaces.api_request import ApiRequestInterface
from instagram_api.signatures import Signatures

__all__ = ['CollectionBase']


class CollectionBase:

    def __init__(self, ig):
        from instagram_api.instagram import Instagram
        self._ig: Instagram = ig

    @staticmethod
    def _paginate_with_exclusion(request: ApiRequestInterface,
                                 exclude_list: List[int],
                                 rank_token: str,
                                 limit: int = 30) -> ApiRequestInterface:
        assert Signatures.is_valid_uuid(rank_token), f'`{rank_token}` is not a valid rank token.'

        # Что-то тут не так в логике
        if not exclude_list:
            request.add_params(
                count=str(limit),
            )

        return request.add_params(
            count=str(limit),
            exclude_list=json.dumps(exclude_list, separators=(',', ':')),
            rank_token=rank_token,
        )

    @staticmethod
    def _paginate_with_multi_exclusion(request: ApiRequestInterface,
                                       exclude_groups: Dict[str, List[int]],
                                       rank_token: str,
                                       limit: int = 30) -> ApiRequestInterface:
        assert Signatures.is_valid_uuid(rank_token), f'`{rank_token}` is not a valid rank token.'

        if not exclude_groups:
            request.add_params(
                count=str(limit),
            )

        total_count = 0

        for ids in exclude_groups.values():
            total_count += len(ids)

        return request.add_params(
            count=str(limit),
            exclude_list=json.dumps(exclude_groups, separators=(',', ':')),
            rank_token=rank_token,
        )
