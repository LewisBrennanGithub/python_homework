import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.aceOfSpades = Card("Spades", 1)
        self.twoOfSpades = Card("Spades", 2)
        self.threeOfSpades = Card("Spades", 3)
        self.deck = [self.threeOfSpades]

    def test_card__is_ace(self):
        self.assertEqual(True, CardGame().check_for_ace(self.aceOfSpades))

    def test_card__isnt_ace(self):
        self.assertEqual(False, CardGame().check_for_ace(self.twoOfSpades))

    def test_card__highest(self):
        self.assertEqual(self.threeOfSpades, CardGame().highest_card(self.twoOfSpades, self.threeOfSpades))

    def test_card__total(self):
        self.assertEqual("You have a total of 3", CardGame().cards_total(self.deck))