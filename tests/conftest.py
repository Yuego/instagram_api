import json
import httpretty
import pytest

from instagram_api.constants import Constants


@pytest.fixture(scope='session')
def base_uri(request):
    for key, value in Constants.API_URLS.items():
        Constants.API_URLS[key] = value.replace('https', 'http')

    return Constants.API_URLS[1]
