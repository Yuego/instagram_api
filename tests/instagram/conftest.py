import json
import pytest
import httpretty

from instagram_api.instagram import Instagram
from instagram_api.constants import Constants


@pytest.fixture(scope='session')
def instagram(request):

    storage_config = {
        'storage_class': 'instagram_api.settings.storage.memory.MemoryStorage',
        'storage_config': {},
    }

    return Instagram(storage_config=storage_config)

@httpretty.activate
@pytest.fixture(scope='session', autouse=True)
def httpretty_register_uris(request):
    base_uri = Constants.API_URLS[1].replace('https', 'http')

    def accounts_login_callback(request, uri, response_headers):
        print(uri)
        print(response_headers)

        return json.dumps({
            'username': 'user',
            'pk': 1,
        })

    httpretty.register_uri(
        httpretty.POST,
        ''.join([base_uri, 'accounts/login/']),
        body=accounts_login_callback,
    )
