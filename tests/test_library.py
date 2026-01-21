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


    def test_borrow_book(self):
        self.library.add_book("B002", "OS", "Silberschatz")
        self.library.borrow_book("B002")
        self.assertEqual(self.library.books["B002"]["status"], "borrowed")

    def test_borrow_already_borrowed_book(self):
        self.library.add_book("B003", "CN", "Tanenbaum")
        self.library.borrow_book("B003")
        with self.assertRaises(ValueError):
            self.library.borrow_book("B003")

    def test_return_book(self):
        self.library.add_book("B004", "DBMS", "Korth")
        self.library.borrow_book("B004")
        self.library.return_book("B004")
        self.assertEqual(self.library.books["B004"]["status"], "available")


    def test_report_contains_header(self):
        self.library.add_book("B005", "AI", "Russell")
        report = self.library.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        self.library.add_book("B006", "ML", "Murphy")
        report = self.library.generate_report()
        self.assertIn("B006 | ML | Murphy | available", report)
