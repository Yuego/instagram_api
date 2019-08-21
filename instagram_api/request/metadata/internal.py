from typing import List, Optional

from instagram_api import response
from instagram_api.constants import Constants
from instagram_api.media.constraints import ConstraintsFactory
from instagram_api.media.photo import PhotoDetails
from instagram_api.media.video import VideoDetails
from instagram_api.utils import Utils

__all__ = ['InternalMetadata']


class InternalMetadata:
    _photo_details: PhotoDetails
    _video_details: VideoDetails
    _upload_id: str
    _video_upload_urls: List[str]
    _video_upload_response: response.UploadVideoResponse
    _photo_upload_response: response.UploadPhotoResponse
    _direct_threads: str
    _direct_users: str
    _bestie_media: bool
    _story_view_mode: str

    def __init__(self, upload_id: str = None):
        if upload_id is not None:
            self._upload_id = upload_id
        else:
            self._upload_id = Utils.generate_upload_id()

        self._bestie_media = False

    @property
    def story_view_mode(self) -> str:
        return self._story_view_mode

    @story_view_mode.setter
    def story_view_mode(self, view_mode: str):
        assert view_mode in [Constants.STORY_VIEW_MODE_ONCE, Constants.STORY_VIEW_MODE_REPLAYABLE], (
            f'Unknown view mode: {view_mode}.'
        )

        self._story_view_mode = view_mode

    @property
    def photo_details(self) -> PhotoDetails:
        return self._photo_details

    def set_photo_details(self,
                          target_feed: int,
                          photo_filename: str) -> PhotoDetails:
        self._photo_details = PhotoDetails(photo_filename)
        self._photo_details.validate(ConstraintsFactory.create_for(target_feed))

        return self._photo_details

    @property
    def video_details(self) -> VideoDetails:
        return self._video_details

    def set_video_details(self,
                          target_feed: int,
                          video_filename: str) -> VideoDetails:
        self._video_details = VideoDetails(video_filename)
        self._video_details.validate(ConstraintsFactory.create_for(target_feed))

        return self._video_details

    @property
    def video_upload_urls(self) -> List[str]:
        return self._video_upload_urls

    @video_upload_urls.setter
    def video_upload_urls(self, resp: response.UploadJobVideoResponse):
        self._video_upload_urls = []
        if resp.video_upload_urls is not None:
            self._video_upload_urls = resp.video_upload_urls

    @property
    def video_upload_response(self):
        return self._video_upload_response

    @video_upload_response.setter
    def video_upload_response(self, resp: response.UploadVideoResponse):
        self._video_upload_response = resp

    @property
    def photo_upload_response(self) -> response.UploadPhotoResponse:
        return self._photo_upload_response

    @photo_upload_response.setter
    def photo_upload_response(self, resp: response.UploadPhotoResponse):
        self._photo_upload_response = resp

    def set_direct_recipients(self, recipient_users: str = None, thread_ids: str = None) -> 'InternalMetadata':
        assert not (recipient_users and thread_ids), 'You can not mix "users" and "thread".'

        if recipient_users:
            self._direct_users = recipient_users
            self._direct_threads = '[]'

        elif thread_ids:
            self._direct_users = '[]'
            self._direct_threads = thread_ids

        else:
            raise ValueError('Please provide at least one recipient.')

        return self

    @property
    def direct_users(self) -> List[int]:
        return self._direct_users

    @property
    def direct_threads(self) -> List[int]:
        return self._direct_threads

    @property
    def bestie_media(self) -> bool:
        return self._bestie_media

    @bestie_media.setter
    def bestie_media(self, bestie_media: bool):
        self._bestie_media = bestie_media
