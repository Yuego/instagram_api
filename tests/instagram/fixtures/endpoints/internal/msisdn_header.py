import json
import httpretty
import pytest


@httpretty.activate
@pytest.fixture(scope='session')
def internal_msisdn_header_success(request, base_uri):
    httpretty.register_uri(
        httpretty.POST,
        ''.join([base_uri, 'accounts/read_msisdn_header/']),
        body=json.dumps({
            'phone_number': '+79991234567',
            'url': 'http://example.com',
            'remaining_ttl_seconds': 15,
            'ttl': 100,
            'status': 'ok',
        }),
    )


