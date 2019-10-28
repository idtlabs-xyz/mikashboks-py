#!/usr/bin/python
import json
import logging
import os

from oauthlib.oauth2 import TokenExpiredError
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

logger = logging.getLogger(__name__)


class Request:
    """
    Handles requests made within the mikashboks ecosystem
    """

    __instance = None
    client = None

    @staticmethod
    def instance(refresh=False):
        """ Static access method. """
        if refresh:
            Request.__instance = Request()

        if Request.__instance is None:
            Request.__instance = Request()
        return Request.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Request.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Request.__instance = self

    def __init__(self) -> None:
        super().__init__()
        self.auth_url = os.getenv("AUTH_ENDPOINT")
        self.client_id = os.getenv('COGNITO_POOL_CLIENT_ID')
        self.client_secret = os.getenv('COGNITO_POOL_CLIENT_SECRET')
        self.base_url = os.getenv("API_ENDPOINT")

        scopes = []
        for i in os.getenv("SCOPES").split(","):
            url = self.base_url if self.base_url[-1] == '/' else self.base_url + '/'
            scopes.append(url + i)
        logger.info("auth scopes " + str(scopes))

        try:
            self.client = OAuth2Session(
                client=BackendApplicationClient(client_id=self.client_id, scope=scopes),
                scope=scopes,
                auto_refresh_url=self.auth_url
            )
            self.client.fetch_token(token_url=self.auth_url, auth=HTTPBasicAuth(self.client_id, self.client_secret))
        except Exception as e:
            logger.exception("Error setting up oauth session")

    def request(self, endpoint: str, method: str = 'GET', filters: dict = None, embedded: dict = None, func=None,
                page=True, include_params=True) -> dict:
        params = None
        if include_params:
            params = {'max_results': 200}
            if filters:
                params['where'] = json.dumps(filters)
            if embedded:
                params['embedded'] = json.dumps(embedded)

        try:
            response = self.client.request(method, self.base_url + endpoint, params=params)
        except TokenExpiredError:
            Request.instance(refresh=True)
            response = self.client.request(method, self.base_url + endpoint, params=params)

        response.raise_for_status()
        logging.info("Successful result returned " + str(response))

        result = response.json()
        if func and result:
            if "_items" in result:
                logger.info("Processing " + str(result['_meta']['total']) + " records")
                list(map(func, result['_items']))
                if method == 'GET' and page and "_links" in result and "next" in result["_links"]:
                    logger.info("Fetching page: " + str(result['_meta']['page'] + 1))
                    self.request(result["_links"]["next"]['href'], func=func, include_params=False)
        else:
            return result

        return None
