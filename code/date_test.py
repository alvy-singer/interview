from unittest import TestCase, main
from date import DateClass


class DateClassTest(TestCase):
    def test_day_of_year(self):
        # not leap year
        my_date = DateClass(2019, 1, 1)
        self.assertEqual(my_date.day_of_year(), 1)
        my_date = DateClass(2019, 2, 10)
        self.assertEqual(my_date.day_of_year(), 41)
        my_date = DateClass(2019, 6, 11)
        self.assertEqual(my_date.day_of_year(), 162)
        my_date = DateClass(2019, 12, 31)
        self.assertEqual(my_date.day_of_year(), 365)
        # leap year
        my_date = DateClass(2016, 1, 1)
        self.assertEqual(my_date.day_of_year(), 1)
        my_date = DateClass(2016, 2, 10)
        self.assertEqual(my_date.day_of_year(), 41)
        my_date = DateClass(2016, 6, 11)
        self.assertEqual(my_date.day_of_year(), 163)
        my_date = DateClass(2016, 12, 31)
        self.assertEqual(my_date.day_of_year(), 366)


if __name__ == '__main__':
    main()
