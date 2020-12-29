import unittest


from exercises.person import Person


class TestBMI(unittest.TestCase):
    def test_bmi(self):
        bob = Person(50, 5)
        self.assertAlmostEquals(bob.bmi(), 2, places=0)
