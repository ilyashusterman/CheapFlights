

class Flight:

    def __init__(self, flight_number, seats):
        self._flight_number = flight_number
        self._seats = seats
        self.departure_airport = {}
        self.arrival_airport = {}


    def __str__(self):
        return 'Flight: {}'.format(self.__dict__)
