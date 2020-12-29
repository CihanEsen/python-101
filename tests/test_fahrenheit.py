import unittest

from exercises import fahrenheit


class TestFahrenheit(unittest.TestCase):
    def test_conversion(self):
        self.assertAlmostEqual(fahrenheit.conversion(22.5), 72.5, places=1)
