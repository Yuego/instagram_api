import json
import httpretty
import pytest

from instagram_api.client import Client
from instagram_api.request.request import ApiRequest
from instagram_api.constants import Constants
from instagram_api.utils.http import ClientCookieJar


@httpretty.activate
def test_send_request(instagram):
    url = f'{Constants.API_URLS[1]}feed/timeline/'.replace('https', 'http')

    httpretty.register_uri(
        httpretty.GET,
        url,
        json.dumps({
            'message': 'challenge_required',
            'challenge': {
                'url': 'https://i.instagram.com/challenge/16184608445/UD3hGZC5Fx/',
                'api_path': '/challenge/16184608445/UD3hGZC5Fx/',
                'hide_webview_header': True,
                'lock': True,
                'logout': False,
                'native_flow': True
            },
            'status': 'fail',
            'error_type': 'checkpoint_challenge_required'
        })
    )

    c = instagram.client

    # rb = ApiRequest()

    # c = Client(None)

    jar = ClientCookieJar()
    jar.set('test', 'value')

    # c2 = Client(None, cookies=jar)

    response = c(url)

    print(httpretty.last_request())

    # response2 = c2(url, headers=rb.force_headers)

    print(httpretty.last_request())

    d = httpretty

    print(response.status_code)


