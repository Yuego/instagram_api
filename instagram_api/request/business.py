import json

from datetime import date

from instagram_api import response
from instagram_api.constants import Constants

from .base import CollectionBase

__all__ = ['Business']


class Business(CollectionBase):

    def get_insights(self, day: int = None) -> response.InsightsResponse:
        if not day:
            day = date.today().strftime('%d')

        return self._ig.request('insights/account_organic_insights/').add_params(
            show_promotions_in_landing_page='true',
            first=day,
        ).get_response(response.InsightsResponse)

    def get_media_insights(self, media_id: int) -> response.MediaInsightsResponse:
        return self._ig.request(f'insights/media_organic_insights/{media_id}/').add_params(
            ig_sig_key_version=Constants.SIG_KEY_VERSION,
        ).get_response(response.MediaInsightsResponse)

    def get_statistics(self) -> response.GraphQLResponse:
        return self._ig.request('ads/graphql/').set_signed_post(False).set_is_multi_response(True).add_params(
            locale=Constants.USER_AGENT_LOCALE,
            vc_policy='insights_policy',
            surface='account',
            access_token='undefined',
            fb_api_caller_class='RelayModern',
            variables=json.dumps({
                'IgInsightsGridMediaImage_SIZE': 240,
                'timezone': 'Atlantic/Canary',
                'activityTab': True,
                'audienceTab': True,
                'contentTab': True,
                'query_params': json.dumps({
                    'access_token': '',
                    'id': self._ig.account_id,
                })
            })
        ).add_posts(
            doc_id='1926322010754880',
        ).get_response(response.GraphQLResponse)
