import json
import pytest
import httpretty

from instagram_api.instagram import Instagram
from instagram_api.constants import Constants

from .fixtures import *

@pytest.fixture(scope='session')
def instagram(request):

    storage_config = {
        'storage_class': 'instagram_api.settings.storage.memory.MemoryStorage',
        'storage_config': {},
    }

    insta = Instagram(storage_config=storage_config)
    insta.change_user('test_user', 'test_password')

    return insta
