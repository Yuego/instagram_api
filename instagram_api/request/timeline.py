import json
import random
import time

from instagram_api import response

from .base import CollectionBase

__all__ = ['Timeline']


class Timeline(CollectionBase):

    def upload_photo(self, photo_filename: str, external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def upload_video(self, video_filename: str, external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    def upload_album(self, medai: dict, external_metadata: dict = None) -> response.ConfigureResponse:
        ...

    # TODO: перепроверить
    def get_timeline_feed(self, max_id: str = None, options: dict = None) -> response.TimelineFeedResponse:
        async_ads = self._ig.is_experiment_enabled(
            'ig_android_ad_async_ads_universe',
            'is_enabled',
        )

        request = self._ig.request('feed/timeline/').set_signed_post(False).set_is_body_compressed(True).add_headers(**{
            # 'X-CM-Bandwidth-KBPS': '-1.000',
            # 'X-CM-Latency': '0.000',
            'X-Ads-Opt-Out': '0',
            'X-Google-AD-ID': self._ig.advertising_id,
            'X-DEVICE-ID': self._ig.uuid,
        }).add_posts(**{
            '_csrftoken': self._ig.client.get_token(),
            '_uuid': self._ig.uuid,
            'is_prefetch': '0',
            'phone_id': self._ig.phone_id,
            'device_id': self._ig.uuid,
            'client_session_id': self._ig.session_id,
            'battery_level': random.randrange(25, 100),
            'is_charging': '0',
            'will_sound_on': '1',
            'is_on_screen': 'true',
            'timezone_offset': time.timezone,
            'is_async_ads_in_headload_enabled': async_ads and self._ig.is_experiment_enabled(
                'ig_android_ad_async_ads_universe',
                'is_async_ads_in_headload_enabled',
            ),
            'is_async_ads_double_request': async_ads and self._ig.is_experiment_enabled(
                'ig_android_ad_async_ads_universe',
                'is_double_request_enabled'
            ),
            'is_async_ads_rti': async_ads and self._ig.is_experiment_enabled(
                'ig_android_ad_async_ads_universe',
                'is_rti_enabled'
            ),
            'rti_delivery_backend': async_ads and self._ig.get_experiment_param(
                'ig_android_ad_async_ads_universe',
                'rti_delivery_backend'
            ),
        })

        if 'latest_story_pk' in options:
            request.add_posts(**{
                'latest_story_pk': options['latest_story_pk'],
            })

        if max_id is not None:
            request.add_posts(**{
                'reason': 'pagination',
                'max_id': max_id,
                'is_pull_to_refresh': '0',
            })
        elif options.get('is_pull_to_refresh', None):
            request.add_posts(**{
                'reason': 'pull_to_refresh',
                'is_pull_to_refresh': '1',
            })
        elif 'is_pull_to_refresh' in options:
            request.add_posts(**{
                'reason': 'warm_start_fetch',
                'is_pull_to_refresh': '0',
            })
        else:
            request.add_posts(**{
                'reason': 'cold_start_fetch',
                'is_pull_to_refresh': '0',
            })

        if 'seen_posts' in options:
            seen_posts = options['seen_posts']
            if isinstance(seen_posts, (list, tuple, set)):
                seen_posts = ','.join(seen_posts)

            request.add_posts(**{
                'seen_posts': seen_posts,
            })

        elif max_id is None:
            request.add_posts(**{
                'seen_posts': '',
            })

        if 'unseen_posts' in options:
            unseen_posts = options['unseen_posts']
            if isinstance(unseen_posts, (list, tuple, set)):
                unseen_posts = ','.join(unseen_posts)

            request.add_posts(**{
                'unseen_posts': unseen_posts,
            })
        elif max_id is None:
            request.add_posts(**{
                'unseen_posts': '',
            })

        if 'feed_view_info' in options:
            feed_view_info = options['feed_view_info']

            if isinstance(feed_view_info, list):
                feed_view_info = json.dumps(feed_view_info)
            else:
                feed_view_info = json.dumps([feed_view_info])

            request.add_posts(**{
                'feed_view_info': feed_view_info,
            })
        elif max_id is None:
            request.add_posts(**{
                'feed_view_info': '',
            })

        if options.get('push_disabled', None):
            request.add_posts(**{
                'push_disabled': 'true',
            })

        if options.get('recovered_from_crash', None):
            request.add_posts(**{
                'recovered_from_crash': '1',
            })

        return request.get_response(response.TimelineFeedResponse)

    def get_user_feed(self, user_id: int, max_id: str = None) -> response.UserFeedResponse:
        ...

    def get_self_user_feed(self, max_id: str = None) -> response.UserFeedResponse:
        ...

    def get_archived_media_feed(self) -> response.UserFeedResponse:
        ...

    def archive_media(self, media_id: int, only_me: bool = True) -> response.ArchiveMediaResponse:
        ...

    def backup(self, base_output_path: str = None, print_progress: bool = True):
        ...
