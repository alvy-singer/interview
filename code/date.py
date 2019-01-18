MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class DateClass:
    """Date

    Attributes:
        year: An integer indicating year of the date
        month: An integer indicating month of the date
        day: An integer indicating day of the date
    """

    def __init__(self, year, month, day):
        assert isinstance(year, int), 'year must be integer'
        assert year > 0, 'year out of range'
        assert isinstance(month, int), 'month must be integer'
        assert 1 <= month <= 12, 'month out of range'
        assert isinstance(day, int), 'day must be integer'
        assert 1 <= day <= self._days_in_month(year, month), 'day out of range'

        self.year = year
        self.month = month
        self.day = day

    def _is_leap(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def _days_in_month(self, year, month):
        month_day = MONTH_DAYS[month]
        if month == 2 and self._is_leap(year):
            month_day += 1
        return month_day

    def day_of_year(self):
        """the day of the year for that date
        """
        count = 0
        for i in range(0, self.month):
            count += MONTH_DAYS[i]
            if i == 2 and self._is_leap(self.year):
                count += 1
        count += self.day
        return count
