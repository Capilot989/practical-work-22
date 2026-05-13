class AirTicket:
    """
    A class representing an airline ticket with passenger and flight information.

    This class stores all relevant information for an airline ticket including
    passenger details, flight information, seat assignment, and boarding gate.

    Attributes:
        passenger_name (str): Name of the passenger.
        _from (str): Departure airport/city code.
        to (str): Arrival airport/city code.
        date_time (str): Date and time of the flight.
        flight (str): Flight number.
        seat (str): Seat number assigned to the passenger.
        _class (str): Travel class (e.g., Economy, Business, First).
        gate (str): Boarding gate number.
    """
    def __init__(
            self,
            passenger_name,
            _from,
            to,
            date_time,
            flight,
            seat,
            _class,
            gate
    ) -> None:
        """
        Initialize an AirTicket instance.

        Args:
            passenger_name (str): Name of the passenger.
            _from (str): Departure airport/city code.
            to (str): Arrival airport/city code.
            date_time (str): Date and time of the flight.
            flight (str): Flight number.
            seat (str): Seat number assigned to the passenger.
            _class (str): Travel class (e.g., Economy, Business, First).
            gate (str): Boarding gate number.
        """
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __str__(self) -> str:
        """
        Return a formatted string representation of the ticket.

        Returns:
            str: Formatted string with fixed-width columns for each field.
        """
        return (
            f"{self.passenger_name:<15}"
            f"{self._from:<6}"
            f"{self.to:<6}"
            f"{self.date_time:<20}"
            f"{self.flight:<8}"
            f"{self.seat:<6}"
            f"{self._class:<10}"
            f"{self.gate:<5}"
        )


class Load:
    """
    A class for loading airline ticket data from a CSV file.

    This class provides static methods to read ticket data from a semicolon-delimited
    file and create AirTicket objects.

    Class Attributes:
        data (list): A list storing all loaded AirTicket objects.
    """
    data = []

    @staticmethod
    def write(file_name: str) -> None:
        """
        Read ticket data from a CSV file and create AirTicket objects.

        The file should be semicolon-delimited with a header row followed by
        data rows. Each row should contain fields in the following order:
        passenger_name;from;to;date_time;flight;seat;class;gate

        Args:
            file_name (str): Path to the CSV file to read.
        """

        with open(file_name, 'r', encoding='utf-8') as file:

            lines = file.readlines()

            for line in lines[1:]:

                values = line.strip().split(';')

                ticket = AirTicket(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5],
                    values[6],
                    values[7]
                )

                Load.data.append(ticket)
