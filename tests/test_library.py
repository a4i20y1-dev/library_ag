import sys
import os
import unittest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("B001", "Python Basics", "Guido")
        self.assertIn("B001", self.library.books)


if __name__ == "__main__":
    unittest.main()
