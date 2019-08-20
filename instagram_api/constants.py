from .big_strings import *

__all__ = ['Constants']


class Constants:
    API_URLS = {
        1: 'https://i.instagram.com/api/v1/',
        2: 'https://i.instagram.com/api/v2/',
    }

    IG_VERSION = '85.0.0.21.100'
    VERSOIN_CODE = '146536611'

    IG_SIG_KEY = '937463b5272b5d60e9d20f0f8d7d192193dd95095a3ad43725d494300a5ea5fc'
    SIG_KEY_VERSION = '4'

    EXPERIMENTS = EXPERIMENTS
    LOGIN_EXPERIMENTS = LOGIN_EXPERIMENTS
    LAUNCHER_CONFIGS = LAUNCHER_CONFIGS

    USER_AGENT_LOCALE = 'en_US'
    ACCEPT_LANGUAGE = 'en-US'
    ACCEPT_ENCODING = 'gzip,deflate'
    CONTENT_TYPE = 'application/x-www-form-urlencoded; charset=UTF-8'
    X_FB_HTTP_Engine = 'Liger'
    X_IG_Connection_Type = 'WIFI'
    X_IG_Capabilities = '3brTvw=='

    SUPPORTED_CAPABILITIES = [
        {
            'name': 'SUPPORTED_SDK_VERSIONS',
            'value': '13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0,24.0,25.0,26.0,27.0,28.0,29.0,30.0,31.0,'
                     '32.0,33.0,34.0,35.0,36.0,37.0,38.0,39.0,40.0,41.0,42.0,43.0,44.0,45.0,46.0,47.0,48.0,49.0,50.0,'
                     '51.0,52.0,53.0,54.0,55.0,56.0,57.0,58.0',
        },
        {
            'name': 'FACE_TRACKER_VERSION',
            'value': '12',
        },
        {
            'name': 'segmentation',
            'value': 'segmentation_enabled',
        },
        {
            'name': 'COMPRESSION',
            'value': 'ETC2_COMPRESSION',
        },
        {
            'name': 'world_tracker',
            'value': 'world_tracker_enabled',
        },
        {
            'name': 'gyroscope',
            'value': 'gyroscope_enabled',
        },
    ]

    # Facebook Constants.
    FACEBOOK_OTA_FIELDS = FACEBOOK_OTA_FIELDS
    FACEBOOK_ORCA_PROTOCOL_VERSION = 20150314
    FACEBOOK_ORCA_APPLICATION_ID = '124024574287414'
    FACEBOOK_ANALYTICS_APPLICATION_ID = '567067343352427'

    PLATFORM = 'android'
    FBNS_APPLICATION_NAME = 'MQTT'
    INSTAGRAM_APPLICATION_NAME = 'Instagram'
    PACKAGE_NAME = 'com.instagram.android'

    SURFACE_PARAM = [
        4715,
        5734,
    ]

    FEED_TIMELINE = 1
    FEED_TIMELINE_ALBUM = 2
    FEED_STORY = 3
    FEED_DIRECT = 4
    FEED_DIRECT_STORY = 5
    FEED_TV = 6

    STORY_VIEW_MODE_ONCE = 'once'
    STORY_VIEW_MODE_REPLAYABLE = 'replayable'
