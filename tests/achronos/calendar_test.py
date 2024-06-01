import unittest
from achronos import calendar


class CalendarTestCase(unittest.TestCase):
    def test_2024_leapyear(self):
        year = 2024
        is_leap_year = calendar.is_leap_year(year)
        self.assertEqual(is_leap_year, True)

    def test_2000_leapyear(self):
        year = 2000
        is_leap_year = calendar.is_leap_year(year)
        self.assertEqual(is_leap_year, True)  # add assertion here

    def test_weekday_of_day(self):
        d, m, y = (1, 2, 2024)
        wd = calendar.weekday_of_date(d, m, y)
        self.assertEqual(wd, 4)



