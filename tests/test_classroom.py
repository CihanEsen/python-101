import unittest

from exercises.classroom import Classroom


class TestClassroom(unittest.TestCase):
    def test_oldest_student(self):
        geeks = Classroom()
        geeks.add_student("Mary", 15)
        geeks.add_student("Jack", 17)
        geeks.add_student("Sue", 16)

        assert str(geeks.oldest_student()) == 'Person name is Jack and age is 17'
