import unittest

from exercises import dollars


class TestDollars(unittest.TestCase):
    def test_conversion(self):
        self.assertAlmostEqual(dollars.conversion(12), 8.88, places=2)
