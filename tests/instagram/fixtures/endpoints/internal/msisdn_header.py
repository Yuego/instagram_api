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
        adding_headers={
            'Content-Type': 'application/json; charset=utf-8',
            'Vary': 'Accept-Language, Cookie',
            'Content-Language': 'en',
            'Date': 'Sun, 18 Aug 2019 14:51:08 GMT',
            'Strict-Transport-Security': 'max-age=31536000',
            'Cache-Control': 'private, no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
            'X-Frame-Options': 'SAMEORIGIN',
            'content-security-policy': ('report-uri https://www.instagram.com/security/csp_report/; '
                                        'default-src \'self\' https://www.instagram.com; img-src https: data: blob:; '
                                        'font-src https: data:; media-src: https: data:'),
            'X-Content-Type-Options': 'nosniff',
            'X-XSS-Protection': '0',
            'x-aed': '9',
            'X-FB-TRIP-ID': '1679558926',
            'Connection': 'keep-alive',
        }
    )


