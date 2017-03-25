import json
import urllib

import requests
import logging

from RyanairBase import RyanairBase


class RyanairApi(RyanairBase):
    BASE_URL = 'https://api.ryanair.com'
    DESKTOP_BASE_URL = 'https://desktopapps.ryanair.com/v2'

    def __init__(self):
        self._headers = {}
        # self._session_id = SessionToken()

    def get_flight(self, flight_id):
        pass

    def get_flights(self, start_date, end_date, filters):
        pass

    def get_flights_by_country(self, geo_country):
        pass

    def http_get(self, path, params=None, json_body=None):
        logging.debug('send_request({}, {}, {})'.format(path, params, json_body))
        query_string = urllib.urlencode(params) if params else None
        url = '{}{}'.format(self.DESKTOP_BASE_URL, path)
        response = requests.get(url, params=query_string, headers=self._headers, json=json_body)
        assert response.status_code == 200, 'STATUS {}: {}'.format(response.status_code, response.content)
        parsed = json.loads(response.content)
        r = parsed
        assert 'message' not in r, '{}\nparams:{}\nJSON: {}'.format(r, params, json_body)
        return r
