from typing import List, Optional

import json

from instagram_api import response
from instagram_api.exceptions import ThrottledException
from .base import CollectionBase


class People(CollectionBase):

    def get_info_by_id(self, user_id: int, module: str = None) -> response.UserInfoResponse:
        ...

    def get_info_by_name(self, username: str, module: str = 'feed_timeline') -> response.UserInfoResponse:
        ...

    def get_user_id_for_name(self, username: str) -> int:
        ...

    def get_self_info(self) -> response.UserInfoResponse:
        ...

    def get_recent_activity_inbox(self) -> response.ActivityNewsResponse:
        return self._ig.request('news/inbox/').get_response(response.ActivityNewsResponse)

    def get_following_recent_activity(self, max_id: str = None) -> response.FollowingRecentActivityResponse:
        ...

    def get_bootstrap_users(self) -> Optional[response.BootstrapUserResponse]:
        """
        Retrieve bootstrap user data (autocompletion user list).

        WARNING: This is a special, very heavily throttled API endpoint.
        Instagram REQUIRES that you wait several minutes between calls to it.

        :raise: ThrottledException

        :return: response.BootstrapUserResponse or None
        """
        surfaces = [
            'coefficient_direct_closed_friends_ranking',
            'coefficient_direct_recipients_ranking_variant_2',
            'coefficient_rank_recipient_user_suggestion',
            'coefficient_ios_section_test_bootstrap_ranking',
            'autocomplete_user_list',
        ]

        try:
            request = self._ig.request('scores/bootstrap/users/').add_params(
                surfaces=json.dumps(surfaces),
            )

            return request.get_response(response.BootstrapUserResponse)
        except ThrottledException:
            # Throttling is so common that we'll simply return NULL in that case.
            return None

    def get_friendship(self, user_id: int) -> response.FriendshipsShowResponse:
        ...

    def get_friendships(self, user_list: List[int]) -> response.FriendshipsShowManyResponse:
        ...

    def get_pending_friendships(self) -> response.FollowerAndFollowingResponse:
        ...

    def approove_friendship(self, user_id: int) -> response.FriendshipResponse:
        ...

    def reject_friendship(self, user_id: int) -> response.FriendshipResponse:
        ...

    def remove_follower(self, user_id: int) -> response.FriendshipResponse:
        ...

    def mark_user_overage(self, user_id: int) -> response.FriendshipResponse:
        ...

    def get_following(self,
                      user_id: int,
                      rank_token: str,
                      search_query: str = None,
                      max_id: str = None) -> response.FollowerAndFollowingResponse:
        ...

    def get_followers(self,
                      user_id: int,
                      rank_token: str,
                      search_query: str = None,
                      max_id: str = None) -> response.FollowerAndFollowingResponse:
        ...

    def get_self_following(self,
                           rank_token: str,
                           search_query: str = None,
                           max_id: str = None) -> response.FollowerAndFollowingResponse:
        ...

    def get_self_followers(self,
                           rank_token: str,
                           search_query: str = None,
                           max_id: str = None) -> response.FollowerAndFollowingResponse:
        ...

    def search(self,
               query: str,
               exclude_list: List[int] = None,
               rank_token: str = None) -> response.SearchUserResponse:
        ...

    def get_account_details(self, user_id: int) -> response.AccountDetailsResponse:
        ...

    def get_former_usernames(self, user_id: int) -> response.FormerUsernamesResponse:
        ...

    def get_shared_followers(self, user_id: int) -> response.SharedFollowersResponse:
        ...

    def get_active_feed_ads(self, target_user_id: int, max_id: str = None) -> response.ActiveFeedAdsResponse:
        ...

    def get_active_story_ads(self, target_user_id: int, max_id: str = None) -> response.ActiveReelAdsResponse:
        ...

    def link_address_book(self,
                          contacts: dict,
                          module: str = 'find_friends_contacts') -> response.LinkAddressBookResponse:
        ...

    def unlink_address_book(self) -> response.UnlinkAddressBookResponse:
        ...

    def discover_people(self, max_id: str = None) -> response.DiscoverPeopleResponse:
        ...

    def get_suggested_users(self, user_id: int) -> response.SuggestedUsersResponse:
        ...

    def get_suggested_users_badge(self) -> response.SuggestedUsersBadgeResponse:
        ...

    def hide_suggested_user(self, user_id: int, algorithm: str) -> response.SuggestedUsersResponse:
        ...

    def follow(self, user_id: int) -> response.FriendshipResponse:
        ...

    def unfollow(self, user_id: int) -> response.FriendshipResponse:
        ...

    def favorite(self, user_id: int) -> response.GenericResponse:
        ...

    def unfavorite(self, user_id: int) -> response.GenericResponse:
        ...

    def favorite_for_stories(self, user_id: int) -> response.GenericResponse:
        ...

    def unfavorite_for_stories(self, user_id: int) -> response.GenericResponse:
        ...

    def report(self, user_id: int, source_name: str = 'profile') -> response.GenericResponse:
        ...

    def block(self, user_id: int) -> response.FriendshipResponse:
        ...

    def mute_user_media(self, user_id: int, option: str) -> response.FriendshipResponse:
        ...

    def unmute_user_media(self, user_id: int, option: str) -> response.FriendshipResponse:
        ...

    def unblock(self, user_id: int) -> response.FriendshipResponse:
        ...

    def get_blocked_list(self, max_id: str = None) -> response.BlockedListResponse:
        ...

    def block_my_story(self, user_id: int) -> response.FriendshipResponse:
        ...

    def unblock_my_story(self, user_id: int) -> response.FriendshipResponse:
        ...

    def get_blocked_story_list(self) -> response.BlockedReelsResponse:
        ...

    def mute_friend_story(self, user_id: int) -> response.FriendshipResponse:
        ...

    def unmute_friend_story(self, user_id: int) -> response.FriendshipResponse:
        ...

    def get_close_friends(self) -> response.CloseFriendsResponse:
        ...

    def get_suggested_close_friends(self) -> response.CloseFriendsResponse:
        ...

    def set_close_friends(self,
                          add: List[int],
                          remove: List[int],
                          module: str = 'favorites_home_list',
                          source: str = 'audience_manager') -> response.GenericResponse:
        ...
