import unittest
from models.book import *

class TestBook(unittest.TestCase):
    
    def setUp(self):
      self.book1 = Book("book1", "author1", "genre1")
      self.book2 = Book("book2", "author2", "genre2")
      self.book3 = Book("book3", "author3", "genre3")

    def test_book__has_title (self):
      self.assertEqual("book1", self.book1.title)

    def test_book__has_author (self):
      self.assertEqual("author1", self.book1.author)

    def test_book__has_genre (self):
      self.assertEqual("genre1", self.book1.genre)

    def test_book__is_checked_in (self):
      self.assertEqual(False, self.book1.checked_out)