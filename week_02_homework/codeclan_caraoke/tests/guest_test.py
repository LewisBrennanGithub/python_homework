import unittest
from src.guest import *
from src.venue import *
from src.room import *
from src.drink import *
from src.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.venue1 = Venue("Funkin Folk", 5, 500)
        self.drink1 = Drink("IPA", 10)
        self.guest1 = Guest("Clive", 20)

    def test_guest__has_name(self):
        self.assertEqual("Clive", self.guest1.name)

    def test_guest__has_cash(self):
        self.assertEqual(20, self.guest1.cash)

    def test_guest__can_enter(self):
        self.guest1.guest_buy_entry(self.venue1)
        self.assertEqual(15, self.guest1.cash)

    def test_guest__can_enter_and_buy_drink(self):
        self.guest1.guest_buy_entry(self.venue1)
        self.guest1.guest_buy_drink(self.drink1)
        self.assertEqual(5, self.guest1.cash)

    def test_guest__cant_afford_anything_else(self):
        self.guest1.guest_buy_entry(self.venue1)
        self.guest1.guest_buy_drink(self.drink1)
        self.guest1.guest_buy_drink(self.drink1)
        self.assertEqual(5, self.guest1.cash)

    