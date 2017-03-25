import argparse
import logging

import pandas

from ryanair.RyanairApi import RyanairApi


class TestFlightReport:

    def __init__(self):
        self._api = RyanairApi()
        self._file_name = 'flights.csv'

    def test_report_flights(self):
        params = {
            'ADT': 1,
            'CHD': 0,
            'DateIn': '2017-04-04',
            'DateOut': '2017-04-10',
            'Destination': 'BGY',
            'FlexDaysIn': 6,
            'FlexDaysOut': 6,
            'INF': 0,
            'Origin': 'TLV',
            'RoundTrip': 'true',
            'TEEN': 0
        }
        response = self._api.http_get('/en-gb/availability', params=params)
        data_frame = pandas.DataFrame(response['trips'])
        data_frame.to_csv(self._file_name, index=False, encoding='utf-8-sig')

    @classmethod
    def main(cls):
        parser = argparse.ArgumentParser()
        commands = parser.add_mutually_exclusive_group(required=True)
        commands.add_argument('--download', action='store_true')
        parser.add_argument('--csv', '--filename', default=None,
                            help='Custom output/input CSV filename, by default report.csv')
        parser.add_argument('--dry-run', action='store_true',
                            help='Parse the data but do not commit to the database.')
        args = parser.parse_args()
        report = cls()
        if args.download:
            report.test_report_flights()
        elif args.insert:
            raise NotImplementedError()
        else:
            logging.info('Nothing to do.')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    TestFlightReport.main()
