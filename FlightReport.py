import argparse
import json
import logging

import pandas

from ryanair.RyanairApi import RyanairApi


class FlightReport:

    def __init__(self):
        self._api = RyanairApi()
        self._file_name = 'flights.csv'
        self._properties = self.get_properties()

    def get_properties(self):
        with open('properties.json') as data_file:
            params = json.load(data_file)
        return params

    def finder_report_flights(self):
        response = self._api.http_get('/farefinder/3/roundTripFares', params=self._properties['finder'])
        logging.info('Found {} total flights'.format(response['total']))
        logging.info('Fares of {} total'.format(len(response['fares'])))
        data_frame = pandas.DataFrame(response['fares'])
        data_frame.to_csv(self._file_name, index=False, encoding='utf-8-sig')
        logging.info('Report Saved to csv')

    def get_report_flights(self):
        response = self._api.http_get('/en-gb/availability', params=self._properties['report'], environment='desktop')
        data_frame = pandas.DataFrame(response['trips'])
        data_frame.to_csv(self._file_name, index=False, encoding='utf-8-sig')

    @classmethod
    def main(cls):
        parser = argparse.ArgumentParser()
        commands = parser.add_mutually_exclusive_group(required=True)
        commands.add_argument('--download', action='store_true')
        commands.add_argument('--finder', action='store_true')
        parser.add_argument('--csv', '--filename', default=None,
                            help='Custom output/input CSV filename, by default report.csv')
        parser.add_argument('--dry-run', action='store_true',
                            help='Parse the data but do not commit to the database.')
        args = parser.parse_args()
        report = cls()
        if args.download:
            report.get_report_flights()
        elif args.finder:
            report.finder_report_flights()
        elif args.insert:
            raise NotImplementedError()
        else:
            logging.info('Nothing to do.')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    FlightReport.main()
