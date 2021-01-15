import unittest

from exercises.library import Library
from exercises.library import Customer


class TestLibrary(unittest.TestCase):
    def test_borrow(self):
        library = Library()
        library.add_book('Bible')
        library.add_book('Quran')
        library.add_book('Torah')
        john = Customer('John')
        library.borrow('Torah', john)
        assert str(john.list_of_customer_books) == '[Torah]'
        assert str(library.list_of_books) == '[Bible, Quran]'
