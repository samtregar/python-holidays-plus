import unittest

import holidays
import holidays_plus

from datetime import date

class TestBasics(unittest.TestCase):
    def test_pop_named(self):
        self.holidays = holidays.US(years=[2004])
        self.assertIn(date(2004, 1, 1), self.holidays)
        self.holidays.pop_named("New Year's Day")
        self.assertNotIn(date(2004, 1, 1), self.holidays)
        self.assertRaises(KeyError, lambda: self.holidays.pop_named("New Year's Dayz"))

    def test_get_named(self):
        self.holidays = holidays.US(years=[2004])
        self.assertEqual(self.holidays.get_named("New Year's Day"), [date(2004, 1, 1)])
        self.assertEqual(self.holidays.get_named("Nonexistent"), [])

        (day,) = self.holidays.get_named("Martin Luther King Jr. Day")
        self.assertTrue(day)
        
