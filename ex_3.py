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


class User:
    """
        A class representing a user/employee in the meeting system.

        This class stores personal information about a user including their
        identification, nickname, full name, and gender.

        Attributes:
            id (str): Unique identifier for the user.
            nick_name (str): User's nickname or login name.
            first_name (str): User's first name.
            last_name (str): User's last name (surname).
            middle_name (str): User's middle name (patronymic).
            gender (str): User's gender.
        """
    def __init__(
            self,
            user_id: str,
            nick_name: str,
            first_name: str,
            last_name: str,
            middle_name: str,
            gender: str
    ) -> None:
        """
        Initialize a User instance.

        Args:
            user_id (str): Unique identifier for the user.
            nick_name (str): User's nickname or login name.
            first_name (str): User's first name.
            last_name (str): User's last name (surname).
            middle_name (str): User's middle name (patronymic).
            gender (str): User's gender.
        """
        self.id = user_id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender


    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Constructs full name from available name components and formats
        with ID, login, and optional gender.

        Returns:
            str: Formatted user information.
        """
        name = ' '.join(
            item for item in(
                self.last_name,
                self.first_name,
                self.middle_name
            ) if item
        )
        result = (
            f'ID: {self.id} '
            f'LOGIN: {self.nick_name} '
            f'NAME: {name} '
        )
        if self.gender:
            result += f'GENDER: {self.gender}'

        return result
class Meeting:
    """
    A class representing a work meeting.

    This class stores meeting information including participants, date, title,
    and provides methods to count meetings by date and track total meetings.

    Class Attributes:
        lst_meeting (list): Class-level list storing all Meeting instances.

    Attributes:
        id (str): Unique identifier for the meeting.
        date (str or Date): Date of the meeting.
        title (str): Meeting title/subject.
        employees (list): List of User objects attending the meeting.
    """

    lst_meeting = []

    def __init__(self, meeting_id: str, date: str, title: str) -> None:
        """
        Initialize a Meeting instance.

        Args:
            meeting_id (str): Unique identifier for the meeting.
            date (str): Date of the meeting.
            title (str): Meeting title/subject.
        """
        self.id = meeting_id
        self.date = date
        self.title = title
        self.employees = []

    def add_person(self, person: str) -> None:
        """
        Add a person (User) to the meeting participants list.

        Args:
            person (User): The User object to add to the meeting.
        """
        self.employees.append(person)

    @classmethod
    def count_meeting(cls, date):
        """
        Count the number of meetings on a specific date.

        Args:
            date (str): The date to count meetings for.

        Returns:
            int: Number of meetings scheduled on the given date.
        """

        count = 0

        for meeting in cls.lst_meeting:

            if meeting.date == date:
                count += 1

        return count

    @classmethod
    def total(cls):
        """
        Get the total number of meetings created.

        Returns:
            int: Total count of Meeting instances.
        """
        return len(cls.lst_meeting)

    def __str__(self):
        """
        Return a string representation of the meeting.

        Returns:
            str: Formatted meeting information including ID, date, title,
                 and list of all participants.
        """
        employees = '\n'.join(str(person) for person in self.employees)

        return (
            f'Рабочая встреча {self.id}\n'
            f'{self.date} {self.title}\n'
            f'{employees}\n'
        )


class Load:
    """
    A class for loading meeting and user data from CSV files.

    This class provides static methods to read data from three related CSV files:
    - Meetings file
    - Persons (users) file
    - Person-Meeting relationships file

    It creates and links User and Meeting objects accordingly.
    """
    @staticmethod
    def write(meetings_file, persons_file, pers_meetings_file):
        """
        Load meeting and user data from CSV files and establish relationships.

        Args:
            meetings_file (str): Path to the meetings CSV file.
                                Format: id;date;title
            persons_file (str): Path to the persons CSV file.
                               Format: id;nick_name;first_name;last_name;middle_name;gender
            pers_meetings_file (str): Path to the person-meeting relationships CSV file.
                                     Format: meeting_id;person_id

        Note:
            The first line of each CSV file is treated as a header and is skipped.
            All files should use semicolon (;) as delimiter and UTF-8 encoding.
        """
        users = {}
        meetings = {}
        with open(persons_file, 'r', encoding='utf-8') as file:

            lines = file.readlines()

            for line in lines[1:]:
                values = line.strip().split(';')

                user = User(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5]
                )

                users[user.id] = user

        with open(meetings_file, 'r', encoding='utf-8') as file:

            lines = file.readlines()

            for line in lines[1:]:
                values = line.strip().split(';')

                meeting = Meeting(
                    values[0],
                    Date(values[1]),
                    values[2]
                )

                meetings[meeting.id] = meeting
                Meeting.lst_meeting.append(meeting)

        with open(pers_meetings_file, 'r', encoding='utf-8') as file:

            lines = file.readlines()

            for line in lines[1:]:

                values = line.strip().split(';')

                meeting_id = values[0]
                person_id = values[1]

                if meeting_id in meetings and person_id in users:
                    meetings[meeting_id].add_person(
                        users[person_id]
                    )
