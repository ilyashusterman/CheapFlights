from abc import abstractmethod, ABCMeta


class RyanairBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_flights(self, start_date, end_date, filters): pass

    @abstractmethod
    def get_flights_by_country(self, geo_country): pass

    @abstractmethod
    def get_flight(self, flight_id): pass
