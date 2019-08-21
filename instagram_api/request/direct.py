from typing import Optional, List, Union

import json
import re

from pathlib import Path

from instagram_api import response
from instagram_api.constants import Constants
from instagram_api.exceptions import ThrottledException
from instagram_api.request.metadata import InternalMetadata
from instagram_api.signatures import Signatures
from instagram_api.utils import Utils

from .base import CollectionBase

__all__ = ['Direct']


class Direct(CollectionBase):

    def get_inbox(self, cursor_id: Optional[str] = None) -> response.DirectInboxResponse:
        request = self._ig.request('direct_v2/inbox/').add_params(
            persistentBadging='true',
            use_unified_inbox='true',
        )
        if cursor_id is not None:
            request.add_params(cursor=cursor_id)

        return request.get_response(response.DirectInboxResponse)

    def get_pending_inbox(self, cursor_id: Optional[str] = None) -> response.DirectPendingInboxResponse:
        request = self._ig.request('direct_v2/pending_inbox/').add_params(
            persistentBadging='true',
            use_unified_inbox='true',
        )
        if cursor_id is not None:
            request.add_params(cursor=cursor_id)

        return request.get_response(response.DirectPendingInboxResponse)

    # TODO: write test !!!
    @staticmethod
    def _check_numeric_identifiers(ids: list, id_type: type = str):
        assert ids, 'Please provide at least one item.'

        str_ids = []
        for _id in ids[:]:
            try:
                _id = int(_id)
            except ValueError:
                raise ValueError(f'`{_id}` is not a valid identifier.')
            else:
                _id = id_type(_id)

            str_ids.append(_id)

        return str_ids

    def approve_pending_threads(self, threads: list) -> response.GenericResponse:
        threads = self._check_numeric_identifiers(threads)

        if len(threads) > 1:
            request = self._ig.request('direct_v2/ids/approve_multiple/').add_posts(
                thread_ids=json.dumps(threads),
            )
        else:
            thread = threads[0]
            request = self._ig.request(f'direct_v2/ids/{thread}/approve/')

        return request.add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    def decline_pending_threads(self, threads: list) -> response.GenericResponse:
        threads = self._check_numeric_identifiers(threads)

        if len(threads) > 1:
            request = self._ig.request('direct_v2/ids/decline_multiple/').add_posts(
                thread_ids=threads,
            )
        else:
            thread = threads[0]
            request = self._ig.request(f'direct_v2/ids/{thread}/decline/')

        return request.add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    def decline_all_pending_threads(self) -> response.GenericResponse:
        return self._ig.request('direct_v2/ids/decline_all/').add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    def get_presences(self) -> response.PresencesResponse:
        return self._ig.request('direct_v2/get_presence/').get_response(response.PresencesResponse)

    def get_ranked_recipients(self,
                              mode: str,
                              show_threads: bool,
                              query: str = None) -> Optional[response.DirectRankedRecipientsResponse]:
        try:
            request = self._ig.request('direct_v2/ranked_recipients/').add_params(
                mode=mode,
                show_threads='true' if show_threads else 'false',
                use_unified_inbox='true',
            )
            if query is not None:
                request.add_params(query=query)

            return request.get_response(response.DirectRankedRecipientsResponse)
        except ThrottledException:
            return None

    def get_thread_by_participants(self, users: List[int]) -> response.DirectThreadResponse:
        assert users, 'Please provide at least one participant.'

        users = self._check_numeric_identifiers(users, int)

        return self._ig.request('direct_v2/threads/get_by_participants/').add_params(
            recipient_users=json.dumps(users, separators=(',', ':')),
        ).get_response(response.DirectThreadResponse)

    def get_thread(self, thread_id: int, cursor_id: Optional[str] = None) -> response.DirectThreadResponse:
        request = self._ig.request(f'direct_v2/threads/{thread_id}/').add_params(
            use_unified_inbox='true',
        )
        if cursor_id is not None:
            request.add_params(cursor=cursor_id)

        return request.get_response(response.DirectThreadResponse)

    def get_visual_thread(self,
                          thread_id: int,
                          cursor_id: Optional[str] = None) -> response.DirectVisualThreadResponse:
        request = self._ig.request(f'direct_v2/visual_threads/{thread_id}/')

        if cursor_id is not None:
            request.add_params(cursor=cursor_id)

        return request.get_response(response.DirectVisualThreadResponse)

    def update_thread_title(self, thread_id: int, title: str) -> response.DirectThreadResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/update_title/').add_posts(
            _uuid=self._ig.uuid,
            _csrftoken=self._ig.client.get_token(),
            title=title.strip(),
        ).set_signed_post(False).get_response(response.DirectThreadResponse)

    def mute_thread(self, thread_id: int) -> response.GenericResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/mute/').add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    def unmute_thread(self, thread_id: int) -> response.GenericResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/unmute/').add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    def create_group_thread(self,
                            user_ids: List[int],
                            thread_title: str) -> response.DirectCreateGroupThreadResponse:
        user_ids = self._check_numeric_identifiers(user_ids)

        return self._ig.request('direct_v2/create_group_thread/').add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
            recipient_users=json.dumps(user_ids),
            _uid=self._ig.account_id,
            thread_title=thread_title,
        ).get_response(response.DirectCreateGroupThreadResponse)

    def add_users_to_thread(self, thread_id: int, users: List[int]) -> response.DirectThreadResponse:
        users = self._check_numeric_identifiers(users)

        return self._ig.request(f'direct_v2/threads/{thread_id}/add_user/').add_posts(
            _csrftoken=self._ig.client.get_token(),
            user_ids=json.dumps(users),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.DirectThreadResponse)

    def leave_thread(self, thread_id: int) -> response.GenericResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/leave/').add_posts(
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    def hide_thread(self, thread_id: int) -> response.GenericResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/hide/').add_posts(
            use_unified_inbox='true',
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).set_signed_post(False).get_response(response.GenericResponse)

    # TODO: write test !!!
    def _prepare_recipients(self,
                            users: List[int] = None,
                            thread: int = None,
                            use_quotes: bool = False,
                            limit: int = 32) -> dict:
        assert users or thread, 'Please provide at least one recipient (`users` or `thread`).'
        assert not (users and thread), 'You can not mix "users" and "thread".'

        result = {}

        if users:
            assert isinstance(users, (list, tuple, set)), '"users" must be a list instance.'
            assert len(users) <= limit, f'You can specify up to {limit} recipients.'

            users = self._check_numeric_identifiers(users, int)

            result['recipient_users'] = '[[%s]]' % ','.join(users)

        if thread:
            threads = self._check_numeric_identifiers([thread], str if use_quotes else int)

            result['thread_ids'] = json.dumps(threads, separators=(',', ':'))

        return result

    # TODO: write test
    def _send_direct_item(self,
                          item_type: str,
                          users: List[int] = None,
                          thread: int = None,
                          **options):
        options = options or {}

        signed_post = False

        if item_type == 'message':
            assert options.get('text', None), 'No text message provided'

            request = self._ig.request('direct_v2/threads/broadcast/text/').add_posts(
                text=options['text']
            )

        elif item_type == 'like':
            request = self._ig.request('direct_v2/threads/broadcast/like/')

        elif item_type == 'hashtag':
            assert options.get('text', None), 'No hashtag provided.'

            request = self._ig.request('direct_v2/threads/broadcast/hashtag/').add_posts(
                hashtag=options['hashtag'],
            )

            if options.get('text', None):
                request.add_posts(text=options['text'])

        elif item_type == 'location':
            assert options.get('venue_id', None), 'No venue_id provided.'

            request = self._ig.request('direct_v2/threads/broadcast/location/').add_posts(
                venue_id=options['venue_id'],
            )

            if options.get('text', None):
                request.add_posts(text=options['text'])

        elif item_type == 'profile':
            assert options.get('profile_user_id', None), 'No profile_user_id provided.'

            request = self._ig.request('direct_v2/threads/broadcast/profile/').add_posts(
                profile_user_id=options['profile_user_id'],
            )

            if options.get('text', None):
                request.add_posts(text=options['text'])

        elif item_type == 'photo':
            assert options.get('filepath', None), 'No filepath provided.'

            request = self._ig.request('direct_v2/threads/broadcast/upload_photo/').add_file(
                key='photo',
                path=options['filepath'],
                name=f'direct_temp_photo_{Utils.generate_upload_id()}.jpg'
            )

        elif item_type == 'video':
            assert options.get('upload_id', None), 'No upload_id provided.'

            request = self._ig.request('direct_v2/threads/broadcast/configure_video/').add_posts(
                upload_id=options['upload_id'],
            )

            if options.get('video_result', None):
                request.add_posts(
                    video_result=options['video_result'],
                )

        elif item_type == 'links':
            assert options.get('link_urls', None), 'No link_urls provided.'
            assert options.get('link_text', None), 'No link_text provided.'

            request = self._ig.request('direct_v2/threads/broadcast/link/').add_posts(
                link_urls=options['link_urls'],
                link_text=options['link_text'],
            )

        elif item_type == 'reaction':
            params = {}
            for key in ['reaction_type', 'reaction_status', 'item_id', 'node_type']:
                assert options.get(key, None), f'No `{key}` provided.'

                params[key] = options[key]

            request = self._ig.request('direct_v2/threads/broadcast/reaction/').add_posts(**params)

        elif item_type == 'live':
            assert options.get('broadcast_id', None), 'No broadcast_id provided.'

            request = self._ig.request('direct_v2/threads/broadcast/live_viewer_invite/').add_posts(
                broadcast_id=options['broadcast_id'],
            )

            if options.get('text', None):
                request.add_posts(text=options['text'])

        else:
            raise AssertionError('Unsupported _send_direct_item() type.')

        recipients = self._prepare_recipients(users, thread, False)
        request.add_posts(**recipients)

        if 'client_context' not in options:
            options['client_context'] = Signatures.generate_uuid(True)
        elif not Signatures.is_valid_uuid(options['client_context']):
            raise AssertionError('`%s` is not valid UUID.' % options['client_context'])

        if signed_post:
            request.add_posts(_uid=self._ig.account_id)

        return request.set_signed_post(signed_post).add_posts(
            action='send_item',
            client_context=options['client_context'],
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).get_response(response.DirectSendItemResponse)

    def _send_direct_items(self,
                           items_type: str,
                           users: List[int] = None,
                           thread: int = None,
                           **options,
                           ):
        signed_post = False

        if items_type == 'media_share':
            assert options.get('media_id', None), 'No media_id provided.'

            request = self._ig.request('direct_v2/threads/broadcast/media_share/').add_posts(
                media_id=options['media_id'],
            )

            if options.get('text', None):
                request.add_posts(text=options['text'])

            if 'media_type' in options and options['media_type'] == 'video':
                request.add_params(media_type='video')
            else:
                request.add_params(media_type='photo')

        elif items_type == 'story_share':
            assert options.get('story_media_id', None), 'No media_id provided.'

            request = self._ig.request('direct_v2/threads/broadcast/story_share/').add_posts(
                story_media_id=options['story_media_id'],
            )

            if options.get('reel_id', None):
                request.add_posts(reel_id=options['reel_id'])

            if options.get('text', None):
                request.add_posts(text=options['text'])

            if 'media_type' in options and options['media_type'] == 'video':
                request.add_params(media_type='video')
            else:
                request.add_params(media_type='photo')

        else:
            raise AssertionError('Unsupported _send_direct_items() type.')

        # TODO: refactor this lines (deduplicate, optimize)
        recipients = self._prepare_recipients(users, thread, False)
        request.add_posts(**recipients)

        if 'client_context' not in options:
            options['client_context'] = Signatures.generate_uuid(True)
        elif not Signatures.is_valid_uuid(options['client_context']):
            raise AssertionError('`%s` is not valid UUID.' % options['client_context'])

        if signed_post:
            request.add_posts(_uid=self._ig.account_id)

        return request.set_signed_post(signed_post).add_posts(
            action='send_item',
            unified_broadcast_format='1',
            client_context=options['client_context'],
            _csrftoken=self._ig.client.get_token(),
            _uuid=self._ig.uuid,
        ).get_response(response.DirectSendItemsResponse)

    def _handle_reaction(self,
                         thread_id: int,
                         thread_item_id: int,
                         reaction_type: str,
                         reaction_status: str,
                         **options):
        assert reaction_type in ['like'], f'`{reaction_type}` is not a supported reaction type'

        thread_id = self._check_numeric_identifiers([thread_id], int)[0]
        thread_item_id = self._check_numeric_identifiers([thread_item_id], int)[0]

        return self._send_direct_item(
            item_type='reaction',
            thread=thread_id,
            reaction_type=reaction_type,
            reaction_status=reaction_status,
            item_id=thread_item_id,
            node_type='item',
            **options,
        )

    def send_text(self, text: str,
                  users: List[int] = None,
                  thread: int = None,
                  **options) -> response.DirectSendItemResponse:

        assert text, 'Text can not be empty'
        options = options or {}

        urls = Utils.extract_urls(text)
        options = options.copy()
        if urls:
            options.update({
                'link_urls': json.dumps([u['full_url'] for u in urls]),
                'link_text': text,
            })
        else:
            options.update({
                'text': text,
            })

        return self._send_direct_item(
            item_type='links',
            users=users,
            thread=thread,
            **options,
        )

    def send_post(self,
                  media_id: int,
                  users: List[int] = None,
                  thread: int = None,
                  **options) -> response.DirectSendItemsResponse:
        assert re.match(r'^\d+_\d+$', media_id), f'`{media_id}` is not a valid media ID.'
        assert options.get('media_type', None), 'Please provide media_type in options.'
        assert options['media_type'] in ['photo', 'video'], '`%s` is not a valid media_type.' % options['media_type']

        options['media_id'] = media_id,

        return self._send_direct_items(
            items_type='media_share',
            users=users,
            thread=thread,
            **options,
        )

    def send_photo(self,
                   photo_filename: str,
                   users: List[int] = None,
                   thread: int = None,
                   **options) -> response.DirectSendItemResponse:
        assert photo_filename, 'Not `photo_filename` provided.'
        photo_path = Path(photo_filename)
        if not photo_path.exists() or not photo_path.is_file():
            raise OSError(f'File {photo_filename} is not available for reading.')

        options['filepath'] = photo_filename

        return self._send_direct_item(
            item_type='photo',
            users=users,
            thread=thread,
            **options,
        )

    def send_disappearing_photo(self,
                                photo_filename: str,
                                users: List[int] = None,
                                thread: int = None,
                                external_metadata: dict = None) -> response.ConfigureResponse:

        internal_metadata = InternalMetadata()
        internal_metadata.set_direct_recipients(**self._prepare_recipients(users, thread, True))
        internal_metadata.story_view_mode = Constants.STORY_VIEW_MODE_ONCE

        return self._ig.internal.upload_single_photo(
            target_feed=Constants.FEED_DIRECT_STORY,
            photo_filename=photo_filename,
            internal_metadata=internal_metadata,
            external_metadata=external_metadata,
        )

    def send_replayable_photo(self,
                              photo_filename: str,
                              users: List[int] = None,
                              thread: int = None,
                              external_metadata: dict = None) -> response.ConfigureResponse:

        internal_metadata = InternalMetadata()
        internal_metadata.set_direct_recipients(**self._prepare_recipients(users, thread, True))
        internal_metadata.story_view_mode = Constants.STORY_VIEW_MODE_REPLAYABLE

        return self._ig.internal.upload_single_photo(
            target_feed=Constants.FEED_DIRECT_STORY,
            photo_filename=photo_filename,
            internal_metadata=internal_metadata,
            external_metadata=external_metadata,
        )

    def send_video(self,
                   video_filename: str,
                   users: List[int] = None,
                   thread: int = None,
                   **options) -> response.DirectSendItemResponse:
        ...

    def send_disappearing_video(self,
                                video_filename: str,
                                users: List[int] = None,
                                thread: int = None,
                                external_metadata: dict = None) -> response.ConfigureResponse:

        internal_metadata = InternalMetadata()
        internal_metadata.set_direct_recipients(**self._prepare_recipients(users, thread, True))
        internal_metadata.story_view_mode = Constants.STORY_VIEW_MODE_ONCE

        return self._ig.internal.upload_single_video(
            target_feed=Constants.FEED_DIRECT_STORY,
            video_filename=video_filename,
            internal_metadata=internal_metadata,
            external_metadata=external_metadata,
        )

    def send_replayable_video(self,
                              video_filename: str,
                              users: List[int] = None,
                              thread: int = None,
                              external_metadata: dict = None) -> response.ConfigureResponse:

        internal_metadata = InternalMetadata()
        internal_metadata.set_direct_recipients(**self._prepare_recipients(users, thread, True))
        internal_metadata.story_view_mode = Constants.STORY_VIEW_MODE_ONCE

        return self._ig.internal.upload_single_video(
            target_feed=Constants.FEED_DIRECT_STORY,
            video_filename=video_filename,
            internal_metadata=internal_metadata,
            external_metadata=external_metadata,
        )

    def send_like(self,
                  users: List[int] = None,
                  thread: int = None,
                  **options) -> response.DirectSendItemResponse:
        return self._send_direct_item(
            item_type='like',
            users=users,
            thread=thread,
            **options,
        )

    def send_hashtag(self,
                     hashtag: str,
                     users: List[int] = None,
                     thread: int = None,
                     **options) -> response.DirectSendItemResponse:
        assert hashtag, 'Hashtag can not be epmty.'

        options['hashtag'] = hashtag

        return self._send_direct_item(
            item_type='hashtag',
            users=users,
            thread=thread,
            **options,
        )

    def send_location(self,
                      location_id: int,
                      users: List[int] = None,
                      thread: int = None,
                      **options) -> response.DirectSendItemResponse:
        location_id = self._check_numeric_identifiers([location_id], int)[0]

        options['venue_id'] = location_id

        return self._send_direct_item(
            item_type='location',
            users=users,
            thread=thread,
            **options,
        )

    def send_profile(self,
                     user_id: int,
                     users: List[int] = None,
                     thread: int = None,
                     **options) -> response.DirectSendItemResponse:
        user_id = self._check_numeric_identifiers([user_id], int)[0]

        options['profile_user_id'] = user_id

        return self._send_direct_item(
            item_type='profile',
            users=users,
            thread=thread,
            **options,
        )

    def send_reaction(self,
                      thread_id: int,
                      thread_item_id: int,
                      reaction_type: str,
                      **options) -> response.DirectSendItemResponse:
        return self._handle_reaction(
            thread_id=thread_id,
            thread_item_id=thread_item_id,
            reaction_type=reaction_type,
            reaction_status='created',
            **options,
        )

    def send_story(self,
                   story_id: str,
                   media_type: str,
                   reel_id: str = None,
                   users: List[int] = None,
                   thread: int = None,
                   **options) -> response.DirectSendItemsResponse:
        assert re.match(r'^\d+_\d+$', story_id), f'`{story_id}` is not a valid story ID.'
        assert media_type in ['photo', 'video'], f'`{media_type}` is not a valid media_type'

        if reel_id is not None:
            assert re.match(r'^highlight:\d+$', reel_id), f'`{reel_id}` is not valid reel ID.'

            options['reel_id'] = reel_id

        options['story_media_id'] = story_id

        return self._send_direct_items(
            items_type='story_share',
            users=users,
            thread=thread,
            media_type=media_type,
            **options
        )

    def send_live(self,
                  broadcast_id: int,
                  users: List[int] = None,
                  thread: int = None,
                  **options) -> response.DirectSendItemResponse:

        defaults = options.copy()
        defaults.update(dict(
            broadcast_id=broadcast_id,
        ))

        return self._send_direct_item(
            type='live',
            users=users,
            thread=thread,
            **defaults,
        )

    def delete_reaction(self,
                        thread_id: int,
                        thread_item_id: int,
                        reaction_type: str,
                        **options) -> response.DirectSendItemResponse:
        return self._handle_reaction(
            threadid=thread_id,
            thread_item_id=thread_item_id,
            reaction_type=reaction_type,
            reaction_status='deleted',
            **options,
        )

    def delete_item(self, thread_id: int, thread_item_id: int) -> response.GenericResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/items/{thread_item_id}/delete/').add_posts(
            _uuid=self._ig.uuid,
            _csrftoken=self._ig.client.get_token(),
        ).set_signed_post(False).get_response(response.GenericResponse)

    def mark_item_seen(self, thread_id: int, thread_item_id: int) -> response.DirectSendItemResponse:
        return self._ig.request(f'direct_v2/threads/{thread_id}/items/{thread_item_id}/seen/').add_posts(
            use_unified_inbox='true',
            action='mark_seen',
            thread_id=thread_id,
            item_id=thread_item_id,
            _uuid=self._ig.uuid,
            _csrftoken=self._ig.client.get_token(),
        ).set_signed_post(False).get_response(response.DirectSeenItemResponse)

    def mark_visual_items_seen(self,
                               thread_id: int,
                               thread_item_ids: Union[int, List[int]]) -> response.GenericResponse:
        assert thread_item_ids, 'Please provide at least one thread item id'

        if not isinstance(thread_item_ids, (list, tuple, set)):
            thread_item_ids = [thread_item_ids]
        thread_item_ids = self._check_numeric_identifiers(thread_item_ids, int)

        return self._ig.request(f'direct_v2/visual_threads/{thread_id}/item_seen/').add_posts(
            item_ids=json.dumps(thread_item_ids, separators=(',', ':')),
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.GenericResponse)

    def mark_visual_items_replayed(self,
                                   thread_id: int,
                                   thread_item_ids: Union[int, List[int]]) -> response.GenericResponse:
        assert thread_item_ids, 'Please provide at least one thread item id'

        if not isinstance(thread_item_ids, (list, tuple, set)):
            thread_item_ids = [thread_item_ids]
        thread_item_ids = self._check_numeric_identifiers(thread_item_ids, int)

        return self._ig.request(f'direct_v2/visual_threads/{thread_id}/item_replayed/').add_posts(
            item_ids=thread_item_ids,
            _uuid=self._ig.uuid,
            _uid=self._ig.account_id,
            _csrftoken=self._ig.client.get_token(),
        ).get_response(response.GenericResponse)
