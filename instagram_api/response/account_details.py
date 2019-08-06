from .base_response import Response
from .model import (
    AdsInfo,
    FormerUsernameInfo,
    PrimaryCountryInfo,
    SharedFollowerAccountsInfo,
)

__all__ = ['AccountDetailsResponse']


class AccountDetailsResponse(Response):
    JSON_PROPERTY_MAP = {
        'date_joined': str,
        'former_username_info': FormerUsernameInfo,
        'primary_country_info': PrimaryCountryInfo,
        'shared_follower_accounts_info': SharedFollowerAccountsInfo,
        'ads_info': AdsInfo,
    }
