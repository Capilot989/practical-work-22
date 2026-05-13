from datetime import datetime


class Date:
    """
    A class representing a date with validation and comparison operations.

    This class stores dates in "DD.MM.YYYY" format and provides methods for
    conversion, validation, comparison, and formatted output in Russian.

    Class Attributes:
        months (list): List of Russian month abbreviations (index 1-12).

    Attributes:
        _date (str | None): Internal storage of date string in "DD.MM.YYYY" format,
                           or None if the date is invalid.
    """
    months = [
        '', 'янв', 'фев', 'мар',
        'апр', 'май', 'июн',
        'июл', 'авг', 'сен',
        'окт', 'ноя', 'дек'
    ]

    def __init__(self, date: str) -> None:
        """
        Initialize a Date instance.

        Args:
            date (str): Date string in "DD.MM.YYYY" format.
                       Invalid dates print 'ошибка' and set _date to None.
        """
        if Date.is_date(date):
            self._date = date
        else:
            print('ошибка')
            self._date = None

    @property
    def date(self) -> str:
        """
        Get the formatted date string in Russian format.

        Returns:
            str: Formatted date as "DD Month YYYY г." or 'None' if date is invalid.
        """
        if self._date is None:
            return 'None'

        return f'{int(self._date[:2])} {Date.months[int(self._date[3:5])]} {int(self._date[6:])} г.'

    @date.setter
    def date(self, value: str):
        """
        Set a new date value with validation.

        Args:
            value (str): New date string in "DD.MM.YYYY" format.
                        Invalid dates print 'ошибка' and set _date to None.
        """
        if Date.is_date(value):
            self._date = value

        else:
            print('ошибка')
            self._date = None

    def to_timestamp(self) -> int:
        """
        Convert the date to a Unix timestamp.

        Returns:
            int: Unix timestamp (seconds since 1970-01-01 00:00:00 UTC).

        Note:
            Assumes the date is valid. Undefined behavior if _date is None.
        """
        return int(self._to_datetime().timestamp())

    @staticmethod
    def is_date(value: str) -> bool:
        """
        Validate whether a string is a valid date in "DD.MM.YYYY" format.

        Args:
            value (str): The string to validate.

        Returns:
            bool: True if the string is a valid date in the correct format,
                  False otherwise.
        """
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True

        except ValueError:
            return False

    def __str__(self) -> str:
        """
        Return a string representation of the date.

        Returns:
            str: Formatted date as "DD Month YYYY г." or 'None' if invalid.
        """
        if self._date is None:
            return 'None'

        return f'{int(self._date[:2])} {Date.months[int(self._date[3:5])]} {int(self._date[6:])} г.'

    def _to_datetime(self) -> 'datetime':
        """
        Convert the internal date string to a datetime object.

        Returns:
            datetime: datetime object representing the stored date.

        Note:
            Assumes the date is valid. Undefined behavior if _date is None.
        """
        return datetime.strptime(self._date, "%d.%m.%Y")

    def __eq__(self, other: 'Date') -> bool:
        """
        Check if two dates are equal.

        Args:
            other (Date): Another Date object to compare with.

        Returns:
            bool: True if dates are equal, False otherwise.
        """
        return self._to_datetime() == other._to_datetime()

    def __ne__(self, other: 'Date') -> bool:
        """
        Check if two dates are not equal.

        Args:
            other (Date): Another Date object to compare with.

        Returns:
            bool: True if dates are not equal, False otherwise.
        """
        return self._to_datetime() != other._to_datetime()

    def __lt__(self, other: 'Date') -> bool:
        """
        Check if this date is earlier than another date.

        Args:
            other (Date): Another Date object to compare with.

        Returns:
            bool: True if this date is earlier than other, False otherwise.
        """
        return self._to_datetime() < other._to_datetime()

    def __le__(self, other: 'Date') -> bool:
        """
        Check if this date is earlier than or equal to another date.

        Args:
            other (Date): Another Date object to compare with.

        Returns:
            bool: True if this date is earlier than or equal to other, False otherwise.
        """
        return self._to_datetime() <= other._to_datetime()

    def __gt__(self, other: 'Date') -> bool:
        """
        Check if this date is later than another date.

        Args:
            other (Date): Another Date object to compare with.

        Returns:
            bool: True if this date is later than other, False otherwise.
        """
        return self._to_datetime() > other._to_datetime()

    def __ge__(self, other: 'Date') -> bool:
        """
        Check if this date is later than or equal to another date.

        Args:
            other (Date): Another Date object to compare with.

        Returns:
            bool: True if this date is later than or equal to other, False otherwise.
        """
        return self._to_datetime() >= other._to_datetime()
