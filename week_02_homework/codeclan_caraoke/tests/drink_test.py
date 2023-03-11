import unittest
from src.drink import *

class TestDrink(unittest.TestCase):
  
    def setUp(self):
      self.drink1 = Drink("IPA", 10)
      self.drink2 = Drink("Buckfast", 40)

    def test_drink__has_name(self):
      self.assertEqual("Buckfast", self.drink2.name)

    def test_drink__has_price(self):
       self.assertEqual(40, self.drink2.price)