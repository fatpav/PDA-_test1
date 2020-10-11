import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def test_check_for_card(self):
        card1 = Card("Spades", 3)
        self.assertEqual(False, CardGame.check_for_ace(self,card1))

    def test_highest_card(self):
        card1 = Card("Hearts", 5)
        card2 = Card("Hearts", 11)
        self.assertEqual(card2, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):

        card1 = Card("spades", 4)
        card2 = Card("Hearts", 6)
        cards = [card1, card2]
        self.assertEqual("You have a total of 10", CardGame.cards_total(self, cards))