import json
import httpretty
import pytest


@httpretty.activate
@pytest.fixture(scope='session')
def accounts_login_success(request, base_uri):
    httpretty.register_uri(
        httpretty.POST,
        ''.join([base_uri, 'accounts/login/']),
        body=json.dumps({}),
    )
